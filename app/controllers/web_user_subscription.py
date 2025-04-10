from typing import Annotated

from fastapi import APIRouter, Response
from starlette import status

from app.lib.auth_context import web_user
from app.models.db.user import User
from app.models.db.user_subscription import UserSubscriptionTarget
from app.models.types import UserSubscriptionTargetId
from app.services.user_subscription_service import UserSubscriptionService

router = APIRouter(prefix='/api/web/user-subscription')


@router.post('/{target:str}/{target_id:int}/subscribe')
async def subscribe(
    target: UserSubscriptionTarget,
    target_id: UserSubscriptionTargetId,
    _: Annotated[User, web_user()],
):
    await UserSubscriptionService.subscribe(target, target_id)
    return Response(None, status.HTTP_204_NO_CONTENT)


@router.post('/{target:str}/{target_id:int}/unsubscribe')
async def unsubscribe(
    target: UserSubscriptionTarget,
    target_id: UserSubscriptionTargetId,
    _: Annotated[User, web_user()],
):
    await UserSubscriptionService.unsubscribe(target, target_id)
    return Response(None, status.HTTP_204_NO_CONTENT)
