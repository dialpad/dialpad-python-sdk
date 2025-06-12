from typing_extensions import NotRequired, TypedDict


class MeetingParticipantProto(TypedDict):
  """Public API representation of an UberConference meeting participant."""

  call_in_method: NotRequired[str]
  'The method this participant used to joined the meeting.'
  display_name: NotRequired[str]
  'Name of the meeting participant.'
  email: NotRequired[str]
  'The email address of the participant. (if applicable)'
  is_organizer: NotRequired[bool]
  "Whether or not the participant is the meeting's organizer."
  name: NotRequired[str]
  'Name of the meeting participant.'
  phone: NotRequired[str]
  'The number that the participant dialed in from. (if applicable)'
  phone_number: NotRequired[str]
  'The number that the participant dialed in from. (if applicable)'
  talk_time: NotRequired[int]
  'The amount of time this participant was speaking. (in milliseconds)'


class MeetingRecordingProto(TypedDict):
  """Public API representation of an UberConference meeting recording."""

  size: NotRequired[str]
  'Human-readable size of the recording files. (e.g. 14.3MB)'
  url: NotRequired[str]
  'The URL of the audio recording of the meeting.'


class MeetingSummaryProto(TypedDict):
  """Public API representation of an UberConference meeting."""

  duration_ms: NotRequired[int]
  'The duration of the meeting in milliseconds.'
  end_time: NotRequired[str]
  'The time at which the meeting was ended. (ISO-8601 format)'
  host_name: NotRequired[str]
  'The name of the host of the meeting.'
  id: NotRequired[str]
  'The ID of the meeting.'
  participants: NotRequired[list[MeetingParticipantProto]]
  'The list of users that participated in the meeting.'
  recordings: NotRequired[list[MeetingRecordingProto]]
  'A list of recordings from the meeting.'
  room_id: NotRequired[str]
  'The ID of the conference room in which the meeting took place.'
  start_time: NotRequired[str]
  'The time at which the first participant joined the meeting. (ISO-8601 format)'
  title: NotRequired[str]
  'The name of the meeting.'
  transcript_url: NotRequired[str]
  'The URL of the meeting transcript.'


class MeetingSummaryCollection(TypedDict):
  """Collection of rooms for get all room operations."""

  cursor: NotRequired[str]
  'A token used to return the next page of a previous request.\n\nUse the cursor provided in the previous response.'
  items: NotRequired[list[MeetingSummaryProto]]
  'A list of meeting summaries.'
