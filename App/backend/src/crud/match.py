from datetime import date, datetime, timedelta, timezone

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from db.models.match import Match, MatchStatus

from .base import CRUDBase


class CRUDMatch(CRUDBase[Match]):

    def get_for_user(self, db: Session, *, user_id: str) -> list[Match]:
        return (
            db.query(self.model)
            .filter(
                or_(
                    self.model.user_a_id == user_id,
                    self.model.user_b_id == user_id,
                )
            )
            .order_by(self.model.created_at.desc())
            .all()
        )

    def get_active_for_user(self, db: Session, *, user_id: str) -> list[Match]:
        return (
            db.query(self.model)
            .filter(
                or_(
                    self.model.user_a_id == user_id,
                    self.model.user_b_id == user_id,
                ),
                self.model.status == MatchStatus.ACTIVE,
            )
            .all()
        )
    
    def get_pool_for_user(
        self,
        db: Session,
        *,
        user_id: str,
        year: int,
        week: int,
    ) -> list[Match]:
        start, end = self._week_bounds(year, week)

        return (
            db.query(Match)
            .filter(
                and_(
                    Match.created_at >= start,
                    Match.created_at < end,
                    or_(
                        Match.user_a_id == user_id,
                        Match.user_b_id == user_id,
                    ),
                )
            )
            .order_by(Match.created_at.asc())
            .all()
        )

    @staticmethod
    def _week_bounds(year: int, week: int):
        first_day = date.fromisocalendar(year, week, 1)
        start = datetime.combine(first_day, datetime.min.time())
        end = start + timedelta(days=7)
        return start, end

    def end_match(self, db: Session, *, match: Match) -> Match:
        match.status = MatchStatus.PAST
        match.ended_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(match)
        return match

match_crud = CRUDMatch(Match)
