# This is an auto-generated resource package. Please do not edit it directly.

from .access_control_policies_resource import AccessControlPoliciesResource
from .agent_status_event_subscriptions_resource import AgentStatusEventSubscriptionsResource
from .app_settings_resource import AppSettingsResource
from .blocked_numbers_resource import BlockedNumbersResource
from .call_center_operators_resource import CallCenterOperatorsResource
from .call_centers_resource import CallCentersResource
from .call_event_subscriptions_resource import CallEventSubscriptionsResource
from .call_labels_resource import CallLabelsResource
from .call_review_share_links_resource import CallReviewShareLinksResource
from .call_routers_resource import CallRoutersResource
from .callbacks_resource import CallbacksResource
from .calls_resource import CallsResource
from .changelog_event_subscriptions_resource import ChangelogEventSubscriptionsResource
from .channels_resource import ChannelsResource
from .coaching_teams_resource import CoachingTeamsResource
from .company_resource import CompanyResource
from .contact_event_subscriptions_resource import ContactEventSubscriptionsResource
from .contacts_resource import ContactsResource
from .custom_ivrs_resource import CustomIVRsResource
from .departments_resource import DepartmentsResource
from .fax_lines_resource import FaxLinesResource
from .meeting_rooms_resource import MeetingRoomsResource
from .meetings_resource import MeetingsResource
from .numbers_resource import NumbersResource
from .oauth2_resource import OAuth2Resource
from .offices_resource import OfficesResource
from .recording_share_links_resource import RecordingShareLinksResource
from .rooms_resource import RoomsResource
from .schedule_reports_resource import ScheduleReportsResource
from .sms_event_subscriptions_resource import SmsEventSubscriptionsResource
from .sms_resource import SmsResource
from .stats_resource import StatsResource
from .transcripts_resource import TranscriptsResource
from .user_devices_resource import UserDevicesResource
from .users_resource import UsersResource
from .webhooks_resource import WebhooksResource
from .websockets_resource import WebsocketsResource


class DialpadResourcesMixin:
  """Mixin class that provides resource properties for each API resource.

  This mixin is used by the DialpadClient class to provide easy access
  to all API resources as properties.
  """

  @property
  def access_control_policies(self) -> AccessControlPoliciesResource:
    """Returns an instance of AccessControlPoliciesResource.

    Returns:
        A AccessControlPoliciesResource instance initialized with this client.
    """
    return AccessControlPoliciesResource(self)

  @property
  def agent_status_event_subscriptions(self) -> AgentStatusEventSubscriptionsResource:
    """Returns an instance of AgentStatusEventSubscriptionsResource.

    Returns:
        A AgentStatusEventSubscriptionsResource instance initialized with this client.
    """
    return AgentStatusEventSubscriptionsResource(self)

  @property
  def app_settings(self) -> AppSettingsResource:
    """Returns an instance of AppSettingsResource.

    Returns:
        A AppSettingsResource instance initialized with this client.
    """
    return AppSettingsResource(self)

  @property
  def blocked_numbers(self) -> BlockedNumbersResource:
    """Returns an instance of BlockedNumbersResource.

    Returns:
        A BlockedNumbersResource instance initialized with this client.
    """
    return BlockedNumbersResource(self)

  @property
  def call_center_operators(self) -> CallCenterOperatorsResource:
    """Returns an instance of CallCenterOperatorsResource.

    Returns:
        A CallCenterOperatorsResource instance initialized with this client.
    """
    return CallCenterOperatorsResource(self)

  @property
  def call_centers(self) -> CallCentersResource:
    """Returns an instance of CallCentersResource.

    Returns:
        A CallCentersResource instance initialized with this client.
    """
    return CallCentersResource(self)

  @property
  def call_event_subscriptions(self) -> CallEventSubscriptionsResource:
    """Returns an instance of CallEventSubscriptionsResource.

    Returns:
        A CallEventSubscriptionsResource instance initialized with this client.
    """
    return CallEventSubscriptionsResource(self)

  @property
  def call_labels(self) -> CallLabelsResource:
    """Returns an instance of CallLabelsResource.

    Returns:
        A CallLabelsResource instance initialized with this client.
    """
    return CallLabelsResource(self)

  @property
  def call_review_share_links(self) -> CallReviewShareLinksResource:
    """Returns an instance of CallReviewShareLinksResource.

    Returns:
        A CallReviewShareLinksResource instance initialized with this client.
    """
    return CallReviewShareLinksResource(self)

  @property
  def call_routers(self) -> CallRoutersResource:
    """Returns an instance of CallRoutersResource.

    Returns:
        A CallRoutersResource instance initialized with this client.
    """
    return CallRoutersResource(self)

  @property
  def callbacks(self) -> CallbacksResource:
    """Returns an instance of CallbacksResource.

    Returns:
        A CallbacksResource instance initialized with this client.
    """
    return CallbacksResource(self)

  @property
  def calls(self) -> CallsResource:
    """Returns an instance of CallsResource.

    Returns:
        A CallsResource instance initialized with this client.
    """
    return CallsResource(self)

  @property
  def changelog_event_subscriptions(self) -> ChangelogEventSubscriptionsResource:
    """Returns an instance of ChangelogEventSubscriptionsResource.

    Returns:
        A ChangelogEventSubscriptionsResource instance initialized with this client.
    """
    return ChangelogEventSubscriptionsResource(self)

  @property
  def channels(self) -> ChannelsResource:
    """Returns an instance of ChannelsResource.

    Returns:
        A ChannelsResource instance initialized with this client.
    """
    return ChannelsResource(self)

  @property
  def coaching_teams(self) -> CoachingTeamsResource:
    """Returns an instance of CoachingTeamsResource.

    Returns:
        A CoachingTeamsResource instance initialized with this client.
    """
    return CoachingTeamsResource(self)

  @property
  def company(self) -> CompanyResource:
    """Returns an instance of CompanyResource.

    Returns:
        A CompanyResource instance initialized with this client.
    """
    return CompanyResource(self)

  @property
  def contact_event_subscriptions(self) -> ContactEventSubscriptionsResource:
    """Returns an instance of ContactEventSubscriptionsResource.

    Returns:
        A ContactEventSubscriptionsResource instance initialized with this client.
    """
    return ContactEventSubscriptionsResource(self)

  @property
  def contacts(self) -> ContactsResource:
    """Returns an instance of ContactsResource.

    Returns:
        A ContactsResource instance initialized with this client.
    """
    return ContactsResource(self)

  @property
  def custom_ivrs(self) -> CustomIVRsResource:
    """Returns an instance of CustomIVRsResource.

    Returns:
        A CustomIVRsResource instance initialized with this client.
    """
    return CustomIVRsResource(self)

  @property
  def departments(self) -> DepartmentsResource:
    """Returns an instance of DepartmentsResource.

    Returns:
        A DepartmentsResource instance initialized with this client.
    """
    return DepartmentsResource(self)

  @property
  def fax_lines(self) -> FaxLinesResource:
    """Returns an instance of FaxLinesResource.

    Returns:
        A FaxLinesResource instance initialized with this client.
    """
    return FaxLinesResource(self)

  @property
  def meeting_rooms(self) -> MeetingRoomsResource:
    """Returns an instance of MeetingRoomsResource.

    Returns:
        A MeetingRoomsResource instance initialized with this client.
    """
    return MeetingRoomsResource(self)

  @property
  def meetings(self) -> MeetingsResource:
    """Returns an instance of MeetingsResource.

    Returns:
        A MeetingsResource instance initialized with this client.
    """
    return MeetingsResource(self)

  @property
  def numbers(self) -> NumbersResource:
    """Returns an instance of NumbersResource.

    Returns:
        A NumbersResource instance initialized with this client.
    """
    return NumbersResource(self)

  @property
  def oauth2(self) -> OAuth2Resource:
    """Returns an instance of OAuth2Resource.

    Returns:
        A OAuth2Resource instance initialized with this client.
    """
    return OAuth2Resource(self)

  @property
  def offices(self) -> OfficesResource:
    """Returns an instance of OfficesResource.

    Returns:
        A OfficesResource instance initialized with this client.
    """
    return OfficesResource(self)

  @property
  def recording_share_links(self) -> RecordingShareLinksResource:
    """Returns an instance of RecordingShareLinksResource.

    Returns:
        A RecordingShareLinksResource instance initialized with this client.
    """
    return RecordingShareLinksResource(self)

  @property
  def rooms(self) -> RoomsResource:
    """Returns an instance of RoomsResource.

    Returns:
        A RoomsResource instance initialized with this client.
    """
    return RoomsResource(self)

  @property
  def schedule_reports(self) -> ScheduleReportsResource:
    """Returns an instance of ScheduleReportsResource.

    Returns:
        A ScheduleReportsResource instance initialized with this client.
    """
    return ScheduleReportsResource(self)

  @property
  def sms_event_subscriptions(self) -> SmsEventSubscriptionsResource:
    """Returns an instance of SmsEventSubscriptionsResource.

    Returns:
        A SmsEventSubscriptionsResource instance initialized with this client.
    """
    return SmsEventSubscriptionsResource(self)

  @property
  def sms(self) -> SmsResource:
    """Returns an instance of SmsResource.

    Returns:
        A SmsResource instance initialized with this client.
    """
    return SmsResource(self)

  @property
  def stats(self) -> StatsResource:
    """Returns an instance of StatsResource.

    Returns:
        A StatsResource instance initialized with this client.
    """
    return StatsResource(self)

  @property
  def transcripts(self) -> TranscriptsResource:
    """Returns an instance of TranscriptsResource.

    Returns:
        A TranscriptsResource instance initialized with this client.
    """
    return TranscriptsResource(self)

  @property
  def user_devices(self) -> UserDevicesResource:
    """Returns an instance of UserDevicesResource.

    Returns:
        A UserDevicesResource instance initialized with this client.
    """
    return UserDevicesResource(self)

  @property
  def users(self) -> UsersResource:
    """Returns an instance of UsersResource.

    Returns:
        A UsersResource instance initialized with this client.
    """
    return UsersResource(self)

  @property
  def webhooks(self) -> WebhooksResource:
    """Returns an instance of WebhooksResource.

    Returns:
        A WebhooksResource instance initialized with this client.
    """
    return WebhooksResource(self)

  @property
  def websockets(self) -> WebsocketsResource:
    """Returns an instance of WebsocketsResource.

    Returns:
        A WebsocketsResource instance initialized with this client.
    """
    return WebsocketsResource(self)


__all__ = [
  'AccessControlPoliciesResource',
  'AgentStatusEventSubscriptionsResource',
  'AppSettingsResource',
  'BlockedNumbersResource',
  'CallCenterOperatorsResource',
  'CallCentersResource',
  'CallEventSubscriptionsResource',
  'CallLabelsResource',
  'CallReviewShareLinksResource',
  'CallRoutersResource',
  'CallbacksResource',
  'CallsResource',
  'ChangelogEventSubscriptionsResource',
  'ChannelsResource',
  'CoachingTeamsResource',
  'CompanyResource',
  'ContactEventSubscriptionsResource',
  'ContactsResource',
  'CustomIVRsResource',
  'DepartmentsResource',
  'FaxLinesResource',
  'MeetingRoomsResource',
  'MeetingsResource',
  'NumbersResource',
  'OAuth2Resource',
  'OfficesResource',
  'RecordingShareLinksResource',
  'RoomsResource',
  'ScheduleReportsResource',
  'SmsEventSubscriptionsResource',
  'SmsResource',
  'StatsResource',
  'TranscriptsResource',
  'UserDevicesResource',
  'UsersResource',
  'WebhooksResource',
  'WebsocketsResource',
  'DialpadResourcesMixin',
]
