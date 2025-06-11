from typing_extensions import NotRequired, TypedDict


class AvailableLicensesProto(TypedDict):
  """Available licenses."""

  additional_number_lines: NotRequired[int]
  'The number of additional-number lines allocated for this plan.\n\nadditional-number lines are consumed when multiple numbers are assigned to a target. i.e. if any callable entity has more than one direct number, one additional-number line is consumed for each number after the first number. This line type is available for all account types.'
  contact_center_lines: NotRequired[int]
  'The number of contact-center lines allocated for this plan.\n\nContact-center lines are consumed for new users that can serve as call center agents, but does\n*not* include a primary number for the user. This line type is only available for pro and enterprise accounts.'
  fax_lines: NotRequired[int]
  'The number of fax lines allocated for this plan.\n\nFax lines are consumed when a fax number is assigned to a user, office, department etc. Fax lines can be used with or without a physical fax machine, as received faxes are exposed as PDFs in the Dialpad app. This line type is available for all account types.'
  room_lines: NotRequired[int]
  'The number of room lines allocated for this plan.\n\nRoom lines are consumed when a new room with a dedicated number is created. This line type is available for all account types.'
  sell_lines: NotRequired[int]
  'The number of sell lines allocated for this plan.\n\nSell lines are consumed for new users that can serve as call center agents and includes a primary number for that user. This line type is only available for pro and enterprise accounts.'
  talk_lines: NotRequired[int]
  'The number of talk lines allocated for this plan.\n\nTalk lines are consumed when a new user with a primary number is created. This line type is available for all account types, and does not include the ability for the user to be a call center agent.'
  tollfree_additional_number_lines: NotRequired[int]
  'The number of toll-free-additional-number lines allocated for this plan.\n\nThese are functionally equivalent to additional-number lines, except that the number is a toll-free number. This line type is available for all account types.'
  tollfree_room_lines: NotRequired[int]
  "The number of toll-free room lines allocated for this plan.\n\nThese are functionally equivalent to room lines, except that the room's primary number is a toll-free number (subsequent numbers for a given room will still consume additional-number/toll-free-additional-number lines rather than multiple room lines). This line type is available for all account types."
  tollfree_uberconference_lines: NotRequired[int]
  "The number of toll-free uberconference lines allocated for this plan.\n\nUberconference lines are consumed when a direct number is allocated for a User's uberconference room. This line type is available for all account types."
  uberconference_lines: NotRequired[int]
  "The number of uberconference lines available for this office.\n\nUberconference lines are consumed when a direct number is allocated for a User's uberconference room. This line type is available for all account types."


class BillingContactMessage(TypedDict):
  """Billing contact."""

  address_line_1: str
  '[single-line only]\n\nThe first line of the billing address.'
  address_line_2: NotRequired[str]
  '[single-line only]\n\nThe second line of the billing address.'
  city: str
  '[single-line only]\n\nThe billing address city.'
  country: str
  'The billing address country.'
  postal_code: str
  '[single-line only]\n\nThe billing address postal code.'
  region: str
  '[single-line only]\n\nThe billing address region.'


class BillingContactProto(TypedDict):
  """TypedDict representation of the BillingContactProto schema."""

  address_line_1: NotRequired[str]
  '[single-line only]\n\nThe first line of the billing address.'
  address_line_2: NotRequired[str]
  '[single-line only]\n\nThe second line of the billing address.'
  city: NotRequired[str]
  '[single-line only]\n\nThe billing address city.'
  country: NotRequired[str]
  'The billing address country.'
  postal_code: NotRequired[str]
  '[single-line only]\n\nThe billing address postal code.'
  region: NotRequired[str]
  '[single-line only]\n\nThe billing address region.'


class BillingPointOfContactMessage(TypedDict):
  """TypedDict representation of the BillingPointOfContactMessage schema."""

  email: str
  'The contact email.'
  name: str
  '[single-line only]\n\nThe contact name.'
  phone: NotRequired[str]
  'The contact phone number.'


class PlanProto(TypedDict):
  """Billing plan."""

  additional_number_lines: NotRequired[int]
  'The number of additional-number lines allocated for this plan.\n\nadditional-number lines are consumed when multiple numbers are assigned to a target. i.e. if any callable entity has more than one direct number, one additional-number line is consumed for each number after the first number. This line type is available for all account types.'
  balance: NotRequired[str]
  'The remaining balance for this plan.\n\nThe balance will be expressed as string-encoded floating point values and will be provided in terms of USD.'
  contact_center_lines: NotRequired[int]
  'The number of contact-center lines allocated for this plan.\n\nContact-center lines are consumed for new users that can serve as call center agents, but does\n*not* include a primary number for the user. This line type is only available for pro and enterprise accounts.'
  fax_lines: NotRequired[int]
  'The number of fax lines allocated for this plan.\n\nFax lines are consumed when a fax number is assigned to a user, office, department etc. Fax lines can be used with or without a physical fax machine, as received faxes are exposed as PDFs in the Dialpad app. This line type is available for all account types.'
  next_billing_date: NotRequired[int]
  'The UTC timestamp of the start of the next billing cycle.'
  ppu_address: NotRequired[BillingContactProto]
  'The "Place of Primary Use" address.'
  room_lines: NotRequired[int]
  'The number of room lines allocated for this plan.\n\nRoom lines are consumed when a new room with a dedicated number is created. This line type is available for all account types.'
  sell_lines: NotRequired[int]
  'The number of sell lines allocated for this plan.\n\nSell lines are consumed for new users that can serve as call center agents and includes a primary number for that user. This line type is only available for pro and enterprise accounts.'
  talk_lines: NotRequired[int]
  'The number of talk lines allocated for this plan.\n\nTalk lines are consumed when a new user with a primary number is created. This line type is available for all account types, and does not include the ability for the user to be a call center agent.'
  tollfree_additional_number_lines: NotRequired[int]
  'The number of toll-free-additional-number lines allocated for this plan.\n\nThese are functionally equivalent to additional-number lines, except that the number is a toll-free number. This line type is available for all account types.'
  tollfree_room_lines: NotRequired[int]
  "The number of toll-free room lines allocated for this plan.\n\nThese are functionally equivalent to room lines, except that the room's primary number is a toll-free number (subsequent numbers for a given room will still consume additional-number/toll-free-additional-number lines rather than multiple room lines). This line type is available for all account types."
  tollfree_uberconference_lines: NotRequired[int]
  "The number of toll-free uberconference lines allocated for this plan.\n\nUberconference lines are consumed when a direct number is allocated for a User's uberconference room. This line type is available for all account types."
  uberconference_lines: NotRequired[int]
  "The number of uberconference lines available for this office.\n\nUberconference lines are consumed when a direct number is allocated for a User's uberconference room. This line type is available for all account types."
