import copy
from dataclasses import dataclass
from enum import Enum
from urllib.parse import urlencode


class ContentCategory(Enum):
    film = 'Film'
    tv = 'TV'
    sports = 'Sports'
    others = 'Others'


class PolicyAction(Enum):
    allow = 'ALLOW'
    block = 'BLOCK'


class DisputeStatus(Enum):
    none = 'None'
    in_dispute = 'InDispute'
    under_review = 'UnderReview'
    dispute_rejected = 'DisputeRejected'
    dispute_accepted = 'RHDisputeAccepted'
    manual_dispute_accepted = 'ManualDisputeAccepted'


@dataclass()
class MatchInfoRetrieve:
    start_time: int
    end_time: int

    page: int = None
    page_size: int = None

    asset_id: int = None
    video_length_gt: int = None
    video_length_lt: int = None
    filtered_policy_action: list[PolicyAction] = None
    filtered_dispute_status: list[DisputeStatus] = None

    def deep_copy(self):
        return copy.deepcopy(self)

    def set_time_interval(self, startTime: int, endTime: int):
        self.start_time = startTime
        self.end_time = endTime
        return self

    def set_pagination(self, page: int, pageSize: int):
        self.page = page
        self.page_size = pageSize
        return self

    def set_asset_id(self, assetID: int):
        self.asset_id = assetID
        return self

    def set_video_length_interval(self, gt: int = None, lt: int = None):
        self.video_length_gt = gt
        self.video_length_lt = lt

    def set_filtered_policy_action(self, filtered_policy_action: list[PolicyAction]):
        self.filtered_policy_action = filtered_policy_action

    def set_filtered_dispute_status(self, filtered_dispute_status: list[DisputeStatus]):
        self.filtered_dispute_status = filtered_dispute_status

    def conv_query_param(self) -> str:
        params = [
            ('startTime', self.start_time),
            ('endTime', self.end_time),
        ]
        if self.page_size is not None and self.page_size > 0:
            params.append(('pageSize', self.page_size))
        if self.page is not None and self.page > 0:
            params.append(('page', self.page))
        if self.video_length_gt is not None and self.video_length_gt > 0:
            params.append(('videoLengthGt', self.video_length_gt))
        if self.video_length_lt is not None and self.video_length_lt > 0:
            params.append(('videoLengthLt', self.video_length_lt))
        if self.filtered_policy_action is not None:
            for policy_action in self.filtered_policy_action:
                params.append(('policyAction', policy_action.value))
        if self.filtered_dispute_status is not None:
            for dispute_status in self.filtered_dispute_status:
                params.append(('disputeStatus', dispute_status.value))

        return urlencode(params)
