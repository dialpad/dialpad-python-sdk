from .resource import DialpadResource

class StatsExportResource(DialpadResource):
  """StatsExportResource implements python bindings for the Dialpad API's stats endpoints.
  See https://developers.dialpad.com/reference#stats for additional documentation.
  """
  _resource_path = ['stats']

  def post(self, coaching_group=False, days_ago_start=1, days_ago_end=30, is_today=False,
           export_type='stats', stat_type='calls', **kwargs):
    """Initiate a stats export.

    Args:
      coaching_group (bool, optional): Whether or not the the statistics should be for trainees of
                                       the coach with the given target_id.
      days_ago_start (int, optional): Start of the date range to get statistics for. This is the
                                      number of days to look back relative to the current day. Used
                                      in conjunction with days_ago_end to specify a range.
      days_ago_end (int, optional): End of the date range to get statistics for. This is the number
                                    of days to look back relative to the current day. Used in
                                    conjunction with days_ago_start to specify a range.
      is_today (bool, optional): Whether or not the statistics are for the current day.
                                 days_ago_start and days_ago_end are ignored if this is passed in
      export_type ("stats" or "records", optional): Whether to return aggregated statistics (stats),
                                                    or individual rows for each record (records).
      stat_type (str, optional): One of "calls", "texts", "voicemails", "recordings", "onduty",
                                 "csat", "dispositions". The type of statistics to be returned.
      office_id (int, optional): ID of the office to get statistics for. If a target_id and
                                 target_type are passed in this value is ignored and instead the
                                 target is used.
      target_id (int, optional): The ID of the target for which to return statistics.
      target_type (type, optional): One of "department", "office", "callcenter", "user", "room",
                                    "staffgroup", "callrouter", "channel", "coachinggroup",
                                    "unknown". The type corresponding to the target_id.
      timezone (str, optional): Timezone using a tz database name.

    See Also:
      https://developers.dialpad.com/reference#statsapi_processstats
    """

    data = {
      'coaching_group': coaching_group,
      'days_ago_start': str(days_ago_start),
      'days_ago_end': str(days_ago_end),
      'is_today': is_today,
      'export_type': export_type,
      'stat_type': stat_type,
    }

    data.update(kwargs)

    data = {k: v for k, v in data.items() if v is not None}
    return self.request(method='POST', data=data)

  def get(self, export_id):
    """Retrieves the results of a stats export.

    Args:
      export_id (str, required): The export ID returned by the post method.

    See Also:
      https://developers.dialpad.com/reference#statsapi_getstats
    """
    return self.request([export_id])
