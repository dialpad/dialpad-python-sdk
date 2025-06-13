# This is an auto-generated resource package. Please do not edit it directly.

from .async_access_control_policies_resource import AsyncAccessControlPoliciesResource
from .async_agent_status_event_subscriptions_resource import (
  AsyncAgentStatusEventSubscriptionsResource,
)
from .async_app_settings_resource import AsyncAppSettingsResource
from .async_blocked_numbers_resource import AsyncBlockedNumbersResource
from .async_call_center_operators_resource import AsyncCallCenterOperatorsResource
from .async_call_centers_resource import AsyncCallCentersResource
from .async_call_event_subscriptions_resource import AsyncCallEventSubscriptionsResource
from .async_call_labels_resource import AsyncCallLabelsResource
from .async_call_review_share_links_resource import AsyncCallReviewShareLinksResource
from .async_call_routers_resource import AsyncCallRoutersResource
from .async_callbacks_resource import AsyncCallbacksResource
from .async_calls_resource import AsyncCallsResource
from .async_changelog_event_subscriptions_resource import AsyncChangelogEventSubscriptionsResource
from .async_channels_resource import AsyncChannelsResource
from .async_coaching_teams_resource import AsyncCoachingTeamsResource
from .async_company_resource import AsyncCompanyResource
from .async_contact_event_subscriptions_resource import AsyncContactEventSubscriptionsResource
from .async_contacts_resource import AsyncContactsResource
from .async_custom_ivrs_resource import AsyncCustomIVRsResource
from .async_departments_resource import AsyncDepartmentsResource
from .async_fax_lines_resource import AsyncFaxLinesResource
from .async_meeting_rooms_resource import AsyncMeetingRoomsResource
from .async_meetings_resource import AsyncMeetingsResource
from .async_numbers_resource import AsyncNumbersResource
from .async_oauth2_resource import AsyncOAuth2Resource
from .async_offices_resource import AsyncOfficesResource
from .async_recording_share_links_resource import AsyncRecordingShareLinksResource
from .async_rooms_resource import AsyncRoomsResource
from .async_schedule_reports_resource import AsyncScheduleReportsResource
from .async_sms_event_subscriptions_resource import AsyncSmsEventSubscriptionsResource
from .async_sms_resource import AsyncSmsResource
from .async_stats_resource import AsyncStatsResource
from .async_transcripts_resource import AsyncTranscriptsResource
from .async_user_devices_resource import AsyncUserDevicesResource
from .async_users_resource import AsyncUsersResource
from .async_webhooks_resource import AsyncWebhooksResource
from .async_websockets_resource import AsyncWebsocketsResource


class AsyncDialpadResourcesMixin:
  """Mixin class that provides resource properties for each API resource.

  This mixin is used by the DialpadClient class to provide easy access
  to all API resources as properties.
  """

  @property
  def access_control_policies(self) -> AsyncAccessControlPoliciesResource:
    """Returns an instance of AsyncAccessControlPoliciesResource.

    Returns:
        A AsyncAccessControlPoliciesResource instance initialized with this client.
    """
    return AsyncAccessControlPoliciesResource(self)

  @property
  def agent_status_event_subscriptions(self) -> AsyncAgentStatusEventSubscriptionsResource:
    """Returns an instance of AsyncAgentStatusEventSubscriptionsResource.

    Returns:
        A AsyncAgentStatusEventSubscriptionsResource instance initialized with this client.
    """
    return AsyncAgentStatusEventSubscriptionsResource(self)

  @property
  def app_settings(self) -> AsyncAppSettingsResource:
    """Returns an instance of AsyncAppSettingsResource.

    Returns:
        A AsyncAppSettingsResource instance initialized with this client.
    """
    return AsyncAppSettingsResource(self)

  @property
  def blocked_numbers(self) -> AsyncBlockedNumbersResource:
    """Returns an instance of AsyncBlockedNumbersResource.

    Returns:
        A AsyncBlockedNumbersResource instance initialized with this client.
    """
    return AsyncBlockedNumbersResource(self)

  @property
  def call_center_operators(self) -> AsyncCallCenterOperatorsResource:
    """Returns an instance of AsyncCallCenterOperatorsResource.

    Returns:
        A AsyncCallCenterOperatorsResource instance initialized with this client.
    """
    return AsyncCallCenterOperatorsResource(self)

  @property
  def call_centers(self) -> AsyncCallCentersResource:
    """Returns an instance of AsyncCallCentersResource.

    Returns:
        A AsyncCallCentersResource instance initialized with this client.
    """
    return AsyncCallCentersResource(self)

  @property
  def call_event_subscriptions(self) -> AsyncCallEventSubscriptionsResource:
    """Returns an instance of AsyncCallEventSubscriptionsResource.

    Returns:
        A AsyncCallEventSubscriptionsResource instance initialized with this client.
    """
    return AsyncCallEventSubscriptionsResource(self)

  @property
  def call_labels(self) -> AsyncCallLabelsResource:
    """Returns an instance of AsyncCallLabelsResource.

    Returns:
        A AsyncCallLabelsResource instance initialized with this client.
    """
    return AsyncCallLabelsResource(self)

  @property
  def call_review_share_links(self) -> AsyncCallReviewShareLinksResource:
    """Returns an instance of AsyncCallReviewShareLinksResource.

    Returns:
        A AsyncCallReviewShareLinksResource instance initialized with this client.
    """
    return AsyncCallReviewShareLinksResource(self)

  @property
  def call_routers(self) -> AsyncCallRoutersResource:
    """Returns an instance of AsyncCallRoutersResource.

    Returns:
        A AsyncCallRoutersResource instance initialized with this client.
    """
    return AsyncCallRoutersResource(self)

  @property
  def callbacks(self) -> AsyncCallbacksResource:
    """Returns an instance of AsyncCallbacksResource.

    Returns:
        A AsyncCallbacksResource instance initialized with this client.
    """
    return AsyncCallbacksResource(self)

  @property
  def calls(self) -> AsyncCallsResource:
    """Returns an instance of AsyncCallsResource.

    Returns:
        A AsyncCallsResource instance initialized with this client.
    """
    return AsyncCallsResource(self)

  @property
  def changelog_event_subscriptions(self) -> AsyncChangelogEventSubscriptionsResource:
    """Returns an instance of AsyncChangelogEventSubscriptionsResource.

    Returns:
        A AsyncChangelogEventSubscriptionsResource instance initialized with this client.
    """
    return AsyncChangelogEventSubscriptionsResource(self)

  @property
  def channels(self) -> AsyncChannelsResource:
    """Returns an instance of AsyncChannelsResource.

    Returns:
        A AsyncChannelsResource instance initialized with this client.
    """
    return AsyncChannelsResource(self)

  @property
  def coaching_teams(self) -> AsyncCoachingTeamsResource:
    """Returns an instance of AsyncCoachingTeamsResource.

    Returns:
        A AsyncCoachingTeamsResource instance initialized with this client.
    """
    return AsyncCoachingTeamsResource(self)

  @property
  def company(self) -> AsyncCompanyResource:
    """Returns an instance of AsyncCompanyResource.

    Returns:
        A AsyncCompanyResource instance initialized with this client.
    """
    return AsyncCompanyResource(self)

  @property
  def contact_event_subscriptions(self) -> AsyncContactEventSubscriptionsResource:
    """Returns an instance of AsyncContactEventSubscriptionsResource.

    Returns:
        A AsyncContactEventSubscriptionsResource instance initialized with this client.
    """
    return AsyncContactEventSubscriptionsResource(self)

  @property
  def contacts(self) -> AsyncContactsResource:
    """Returns an instance of AsyncContactsResource.

    Returns:
        A AsyncContactsResource instance initialized with this client.
    """
    return AsyncContactsResource(self)

  @property
  def custom_ivrs(self) -> AsyncCustomIVRsResource:
    """Returns an instance of AsyncCustomIVRsResource.

    Returns:
        A AsyncCustomIVRsResource instance initialized with this client.
    """
    return AsyncCustomIVRsResource(self)

  @property
  def departments(self) -> AsyncDepartmentsResource:
    """Returns an instance of AsyncDepartmentsResource.

    Returns:
        A AsyncDepartmentsResource instance initialized with this client.
    """
    return AsyncDepartmentsResource(self)

  @property
  def fax_lines(self) -> AsyncFaxLinesResource:
    """Returns an instance of AsyncFaxLinesResource.

    Returns:
        A AsyncFaxLinesResource instance initialized with this client.
    """
    return AsyncFaxLinesResource(self)

  @property
  def meeting_rooms(self) -> AsyncMeetingRoomsResource:
    """Returns an instance of AsyncMeetingRoomsResource.

    Returns:
        A AsyncMeetingRoomsResource instance initialized with this client.
    """
    return AsyncMeetingRoomsResource(self)

  @property
  def meetings(self) -> AsyncMeetingsResource:
    """Returns an instance of AsyncMeetingsResource.

    Returns:
        A AsyncMeetingsResource instance initialized with this client.
    """
    return AsyncMeetingsResource(self)

  @property
  def numbers(self) -> AsyncNumbersResource:
    """Returns an instance of AsyncNumbersResource.

    Returns:
        A AsyncNumbersResource instance initialized with this client.
    """
    return AsyncNumbersResource(self)

  @property
  def oauth2(self) -> AsyncOAuth2Resource:
    """Returns an instance of AsyncOAuth2Resource.

    Returns:
        A AsyncOAuth2Resource instance initialized with this client.
    """
    return AsyncOAuth2Resource(self)

  @property
  def offices(self) -> AsyncOfficesResource:
    """Returns an instance of AsyncOfficesResource.

    Returns:
        A AsyncOfficesResource instance initialized with this client.
    """
    return AsyncOfficesResource(self)

  @property
  def recording_share_links(self) -> AsyncRecordingShareLinksResource:
    """Returns an instance of AsyncRecordingShareLinksResource.

    Returns:
        A AsyncRecordingShareLinksResource instance initialized with this client.
    """
    return AsyncRecordingShareLinksResource(self)

  @property
  def rooms(self) -> AsyncRoomsResource:
    """Returns an instance of AsyncRoomsResource.

    Returns:
        A AsyncRoomsResource instance initialized with this client.
    """
    return AsyncRoomsResource(self)

  @property
  def schedule_reports(self) -> AsyncScheduleReportsResource:
    """Returns an instance of AsyncScheduleReportsResource.

    Returns:
        A AsyncScheduleReportsResource instance initialized with this client.
    """
    return AsyncScheduleReportsResource(self)

  @property
  def sms_event_subscriptions(self) -> AsyncSmsEventSubscriptionsResource:
    """Returns an instance of AsyncSmsEventSubscriptionsResource.

    Returns:
        A AsyncSmsEventSubscriptionsResource instance initialized with this client.
    """
    return AsyncSmsEventSubscriptionsResource(self)

  @property
  def sms(self) -> AsyncSmsResource:
    """Returns an instance of AsyncSmsResource.

    Returns:
        A AsyncSmsResource instance initialized with this client.
    """
    return AsyncSmsResource(self)

  @property
  def stats(self) -> AsyncStatsResource:
    """Returns an instance of AsyncStatsResource.

    Returns:
        A AsyncStatsResource instance initialized with this client.
    """
    return AsyncStatsResource(self)

  @property
  def transcripts(self) -> AsyncTranscriptsResource:
    """Returns an instance of AsyncTranscriptsResource.

    Returns:
        A AsyncTranscriptsResource instance initialized with this client.
    """
    return AsyncTranscriptsResource(self)

  @property
  def user_devices(self) -> AsyncUserDevicesResource:
    """Returns an instance of AsyncUserDevicesResource.

    Returns:
        A AsyncUserDevicesResource instance initialized with this client.
    """
    return AsyncUserDevicesResource(self)

  @property
  def users(self) -> AsyncUsersResource:
    """Returns an instance of AsyncUsersResource.

    Returns:
        A AsyncUsersResource instance initialized with this client.
    """
    return AsyncUsersResource(self)

  @property
  def webhooks(self) -> AsyncWebhooksResource:
    """Returns an instance of AsyncWebhooksResource.

    Returns:
        A AsyncWebhooksResource instance initialized with this client.
    """
    return AsyncWebhooksResource(self)

  @property
  def websockets(self) -> AsyncWebsocketsResource:
    """Returns an instance of AsyncWebsocketsResource.

    Returns:
        A AsyncWebsocketsResource instance initialized with this client.
    """
    return AsyncWebsocketsResource(self)


__all__ = [
  'AsyncAccessControlPoliciesResource',
  'AsyncAgentStatusEventSubscriptionsResource',
  'AsyncAppSettingsResource',
  'AsyncBlockedNumbersResource',
  'AsyncCallCenterOperatorsResource',
  'AsyncCallCentersResource',
  'AsyncCallEventSubscriptionsResource',
  'AsyncCallLabelsResource',
  'AsyncCallReviewShareLinksResource',
  'AsyncCallRoutersResource',
  'AsyncCallbacksResource',
  'AsyncCallsResource',
  'AsyncChangelogEventSubscriptionsResource',
  'AsyncChannelsResource',
  'AsyncCoachingTeamsResource',
  'AsyncCompanyResource',
  'AsyncContactEventSubscriptionsResource',
  'AsyncContactsResource',
  'AsyncCustomIVRsResource',
  'AsyncDepartmentsResource',
  'AsyncFaxLinesResource',
  'AsyncMeetingRoomsResource',
  'AsyncMeetingsResource',
  'AsyncNumbersResource',
  'AsyncOAuth2Resource',
  'AsyncOfficesResource',
  'AsyncRecordingShareLinksResource',
  'AsyncRoomsResource',
  'AsyncScheduleReportsResource',
  'AsyncSmsEventSubscriptionsResource',
  'AsyncSmsResource',
  'AsyncStatsResource',
  'AsyncTranscriptsResource',
  'AsyncUserDevicesResource',
  'AsyncUsersResource',
  'AsyncWebhooksResource',
  'AsyncWebsocketsResource',
  'DialpadResourcesMixin',
]
