r"""
generated by json2python-models v0.3.0 at Wed Jan 18 10:36:42 2023
command: /home/edgar/.local/bin/json2models -m Daylio localdata/old.json -o generated/daylio.py -f pydantic
"""
from pydantic import BaseModel, Field
from typing import Any, List, Optional, Union


class Daylio(BaseModel):
    version: int
    is_reminder_on: bool = Field(..., alias="isReminderOn")
    custom_moods: List['CustomMood'] = Field(..., alias="customMoods")
    tags: List['Tag']
    day_entries: List['DayEntry'] = Field(..., alias="dayEntries")
    achievements: List['Achievement']
    days_in_row_longest_chain: int = Field(..., alias="daysInRowLongestChain")
    goals: List[Any]
    prefs: List['Pref']
    tag_groups: List[Any]
    metadata: 'Metadatum'
    mood_icons_pack_id: int = Field(..., alias="moodIconsPackId")
    preferred_mood_icons_ids_for_mood_ids_for_icons_pack: 'PreferredMoodIconsIdsForMoodIdsForIconsPack' = Field(
        ..., alias="preferredMoodIconsIdsForMoodIdsForIconsPack")
    assets: List[Any]
    goal_entries: List[Any] = Field(..., alias="goalEntries")
    goal_success_weeks: List[Any] = Field(..., alias="goalSuccessWeeks")
    reminders: List['Reminder']
    writing_templates: List['WritingTemplate'] = Field(
        ..., alias="writingTemplates")
    mood_icons_default_free_pack_id: int = Field(
        ..., alias="moodIconsDefaultFreePackId")


class CustomMood(BaseModel):
    id_: int = Field(..., alias="id")
    custom_name: str
    mood_group_id: int
    mood_group_order: int
    icon_id: int
    predefined_name_id: int
    state: int
    created_at: int = Field(..., alias="createdAt")


class Tag(BaseModel):
    id_: int = Field(..., alias="id")
    name: str
    created_at: int = Field(..., alias="createdAt")
    icon: int
    order: int
    state: int
    id_tag_group: int


class DayEntry(BaseModel):
    id_: int = Field(..., alias="id")
    minute: int
    hour: int
    day: int
    month: int
    year: int
    datetime_: int = Field(..., alias="datetime")
    time_zone_offset: int = Field(..., alias="timeZoneOffset")
    mood: int
    note: str
    note_title: str
    tags: List[int]
    assets: List[Any]


class Achievement(BaseModel):
    name: str
    ac_first_entry_seen: Optional[bool] = Field(None,
                                                alias="AC_FIRST_ENTRY_SEEN")
    ac_first_entry_unlocked_at: Optional[int] = Field(
        None, alias="AC_FIRST_ENTRY_UNLOCKED_AT")
    ac_entries_seen: Optional[bool] = Field(None, alias="AC_ENTRIES_SEEN")
    ac_entries_unlocked_at: Optional[int] = Field(
        None, alias="AC_ENTRIES_UNLOCKED_AT")
    ac_entries_current_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_CURRENT_LEVEL")
    ac_entries_current_value: Optional[int] = Field(
        None, alias="AC_ENTRIES_CURRENT_VALUE")
    ac_entries_last_seen_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_LAST_SEEN_LEVEL")
    ac_entries_bonus_lvl_seen: Optional[bool] = Field(
        None, alias="AC_ENTRIES_BONUS_LVL_SEEN")
    ac_entries_bonus_lvl_unlocked_at: Optional[int] = Field(
        None, alias="AC_ENTRIES_BONUS_LVL_UNLOCKED_AT")
    ac_entries_bonus_lvl_current_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_BONUS_LVL_CURRENT_LEVEL")
    ac_entries_bonus_lvl_current_value: Optional[int] = Field(
        None, alias="AC_ENTRIES_BONUS_LVL_CURRENT_VALUE")
    ac_entries_bonus_lvl_last_seen_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_BONUS_LVL_LAST_SEEN_LEVEL")
    ac_entries_millenniums_seen: Optional[bool] = Field(
        None, alias="AC_ENTRIES_MILLENNIUMS_SEEN")
    ac_entries_millenniums_unlocked_at: Optional[int] = Field(
        None, alias="AC_ENTRIES_MILLENNIUMS_UNLOCKED_AT")
    ac_entries_millenniums_current_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_MILLENNIUMS_CURRENT_LEVEL")
    ac_entries_millenniums_current_value: Optional[int] = Field(
        None, alias="AC_ENTRIES_MILLENNIUMS_CURRENT_VALUE")
    ac_entries_millenniums_last_seen_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_MILLENNIUMS_LAST_SEEN_LEVEL")
    ac_entries_eternity_seen: Optional[bool] = Field(
        None, alias="AC_ENTRIES_ETERNITY_SEEN")
    ac_entries_eternity_unlocked_at: Optional[int] = Field(
        None, alias="AC_ENTRIES_ETERNITY_UNLOCKED_AT")
    ac_entries_eternity_current_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_ETERNITY_CURRENT_LEVEL")
    ac_entries_eternity_current_value: Optional[int] = Field(
        None, alias="AC_ENTRIES_ETERNITY_CURRENT_VALUE")
    ac_entries_eternity_last_seen_level: Optional[int] = Field(
        None, alias="AC_ENTRIES_ETERNITY_LAST_SEEN_LEVEL")
    ac_streak_seen: Optional[bool] = Field(None, alias="AC_STREAK_SEEN")
    ac_streak_unlocked_at: Optional[int] = Field(None,
                                                 alias="AC_STREAK_UNLOCKED_AT")
    ac_streak_current_level: Optional[int] = Field(
        None, alias="AC_STREAK_CURRENT_LEVEL")
    ac_streak_current_value: Optional[int] = Field(
        None, alias="AC_STREAK_CURRENT_VALUE")
    ac_streak_last_seen_level: Optional[int] = Field(
        None, alias="AC_STREAK_LAST_SEEN_LEVEL")
    ac_mega_streak_seen: Optional[bool] = Field(None,
                                                alias="AC_MEGA_STREAK_SEEN")
    ac_mega_streak_unlocked_at: Optional[int] = Field(
        None, alias="AC_MEGA_STREAK_UNLOCKED_AT")
    ac_mega_streak_current_level: Optional[int] = Field(
        None, alias="AC_MEGA_STREAK_CURRENT_LEVEL")
    ac_mega_streak_current_value: Optional[int] = Field(
        None, alias="AC_MEGA_STREAK_CURRENT_VALUE")
    ac_mega_streak_last_seen_level: Optional[int] = Field(
        None, alias="AC_MEGA_STREAK_LAST_SEEN_LEVEL")
    ac_epic_streak_seen: Optional[bool] = Field(None,
                                                alias="AC_EPIC_STREAK_SEEN")
    ac_epic_streak_unlocked_at: Optional[int] = Field(
        None, alias="AC_EPIC_STREAK_UNLOCKED_AT")
    ac_epic_streak_current_level: Optional[int] = Field(
        None, alias="AC_EPIC_STREAK_CURRENT_LEVEL")
    ac_epic_streak_current_value: Optional[int] = Field(
        None, alias="AC_EPIC_STREAK_CURRENT_VALUE")
    ac_epic_streak_last_seen_level: Optional[int] = Field(
        None, alias="AC_EPIC_STREAK_LAST_SEEN_LEVEL")
    ac_mythical_streak_seen: Optional[bool] = Field(
        None, alias="AC_MYTHICAL_STREAK_SEEN")
    ac_mythical_streak_unlocked_at: Optional[int] = Field(
        None, alias="AC_MYTHICAL_STREAK_UNLOCKED_AT")
    ac_mythical_streak_current_level: Optional[int] = Field(
        None, alias="AC_MYTHICAL_STREAK_CURRENT_LEVEL")
    ac_mythical_streak_current_value: Optional[int] = Field(
        None, alias="AC_MYTHICAL_STREAK_CURRENT_VALUE")
    ac_mythical_streak_last_seen_level: Optional[int] = Field(
        None, alias="AC_MYTHICAL_STREAK_LAST_SEEN_LEVEL")
    ac_streak_bonus_seen: Optional[bool] = Field(None,
                                                 alias="AC_STREAK_BONUS_SEEN")
    ac_streak_bonus_unlocked_at: Optional[int] = Field(
        None, alias="AC_STREAK_BONUS_UNLOCKED_AT")
    ac_tags_seen: Optional[bool] = Field(None, alias="AC_TAGS_SEEN")
    ac_tags_unlocked_at: Optional[int] = Field(None,
                                               alias="AC_TAGS_UNLOCKED_AT")
    ac_tags_current_level: Optional[int] = Field(None,
                                                 alias="AC_TAGS_CURRENT_LEVEL")
    ac_tags_current_value: Optional[int] = Field(None,
                                                 alias="AC_TAGS_CURRENT_VALUE")
    ac_tags_last_seen_level: Optional[int] = Field(
        None, alias="AC_TAGS_LAST_SEEN_LEVEL")
    ac_moods_seen: Optional[bool] = Field(None, alias="AC_MOODS_SEEN")
    ac_moods_unlocked_at: Optional[int] = Field(None,
                                                alias="AC_MOODS_UNLOCKED_AT")
    ac_moods_current_level: Optional[int] = Field(
        None, alias="AC_MOODS_CURRENT_LEVEL")
    ac_moods_current_value: Optional[int] = Field(
        None, alias="AC_MOODS_CURRENT_VALUE")
    ac_moods_last_seen_level: Optional[int] = Field(
        None, alias="AC_MOODS_LAST_SEEN_LEVEL")
    ac_goals_dedicated_seen: Optional[bool] = Field(
        None, alias="AC_GOALS_DEDICATED_SEEN")
    ac_goals_dedicated_unlocked_at: Optional[int] = Field(
        None, alias="AC_GOALS_DEDICATED_UNLOCKED_AT")
    ac_goals_dedicated_current_level: Optional[int] = Field(
        None, alias="AC_GOALS_DEDICATED_CURRENT_LEVEL")
    ac_goals_dedicated_current_value: Optional[int] = Field(
        None, alias="AC_GOALS_DEDICATED_CURRENT_VALUE")
    ac_goals_dedicated_last_seen_level: Optional[int] = Field(
        None, alias="AC_GOALS_DEDICATED_LAST_SEEN_LEVEL")
    ac_paparazzi_seen: Optional[bool] = Field(None, alias="AC_PAPARAZZI_SEEN")
    ac_paparazzi_unlocked_at: Optional[int] = Field(
        None, alias="AC_PAPARAZZI_UNLOCKED_AT")
    ac_paparazzi_current_level: Optional[int] = Field(
        None, alias="AC_PAPARAZZI_CURRENT_LEVEL")
    ac_paparazzi_current_value: Optional[int] = Field(
        None, alias="AC_PAPARAZZI_CURRENT_VALUE")
    ac_paparazzi_last_seen_level: Optional[int] = Field(
        None, alias="AC_PAPARAZZI_LAST_SEEN_LEVEL")
    ac_colors_seen: Optional[bool] = Field(None, alias="AC_COLORS_SEEN")
    ac_colors_unlocked_at: Optional[int] = Field(None,
                                                 alias="AC_COLORS_UNLOCKED_AT")
    ac_multiple_entries_seen: Optional[bool] = Field(
        None, alias="AC_MULTIPLE_ENTRIES_SEEN")
    ac_multiple_entries_unlocked_at: Optional[int] = Field(
        None, alias="AC_MULTIPLE_ENTRIES_UNLOCKED_AT")
    ac_groups_seen: Optional[bool] = Field(None, alias="AC_GROUPS_SEEN")
    ac_groups_unlocked_at: Optional[int] = Field(None,
                                                 alias="AC_GROUPS_UNLOCKED_AT")
    ac_style_seen: Optional[bool] = Field(None, alias="AC_STYLE_SEEN")
    ac_style_unlocked_at: Optional[int] = Field(None,
                                                alias="AC_STYLE_UNLOCKED_AT")
    ac_smart_seen: Optional[bool] = Field(None, alias="AC_SMART_SEEN")
    ac_smart_unlocked_at: Optional[int] = Field(None,
                                                alias="AC_SMART_UNLOCKED_AT")
    ac_auto_backup_seen: Optional[bool] = Field(None,
                                                alias="AC_AUTO_BACKUP_SEEN")
    ac_auto_backup_unlocked_at: Optional[int] = Field(
        None, alias="AC_AUTO_BACKUP_UNLOCKED_AT")
    ac_premium_seen: Optional[bool] = Field(None, alias="AC_PREMIUM_SEEN")
    ac_premium_unlocked_at: Optional[int] = Field(
        None, alias="AC_PREMIUM_UNLOCKED_AT")
    ac_rollercoaster_seen: Optional[bool] = Field(
        None, alias="AC_ROLLERCOASTER_SEEN")
    ac_rollercoaster_unlocked_at: Optional[int] = Field(
        None, alias="AC_ROLLERCOASTER_UNLOCKED_AT")
    ac_pin_code_seen: Optional[bool] = Field(None, alias="AC_PIN_CODE_SEEN")
    ac_pin_code_unlocked_at: Optional[int] = Field(
        None, alias="AC_PIN_CODE_UNLOCKED_AT")
    ac_no_backup_seen: Optional[bool] = Field(None, alias="AC_NO_BACKUP_SEEN")
    ac_no_backup_unlocked_at: Optional[int] = Field(
        None, alias="AC_NO_BACKUP_UNLOCKED_AT")
    ac_meh_days_seen: Optional[bool] = Field(None, alias="AC_MEH_DAYS_SEEN")
    ac_meh_days_unlocked_at: Optional[int] = Field(
        None, alias="AC_MEH_DAYS_UNLOCKED_AT")
    ac_good_days_seen: Optional[bool] = Field(None, alias="AC_GOOD_DAYS_SEEN")
    ac_good_days_unlocked_at: Optional[int] = Field(
        None, alias="AC_GOOD_DAYS_UNLOCKED_AT")
    ac_rad_days_seen: Optional[bool] = Field(None, alias="AC_RAD_DAYS_SEEN")
    ac_rad_days_unlocked_at: Optional[int] = Field(
        None, alias="AC_RAD_DAYS_UNLOCKED_AT")
    ac_moods_bonus_seen: Optional[bool] = Field(None,
                                                alias="AC_MOODS_BONUS_SEEN")
    ac_moods_bonus_unlocked_at: Optional[int] = Field(
        None, alias="AC_MOODS_BONUS_UNLOCKED_AT")
    ac_tags_bonus_seen: Optional[bool] = Field(None,
                                               alias="AC_TAGS_BONUS_SEEN")
    ac_tags_bonus_unlocked_at: Optional[int] = Field(
        None, alias="AC_TAGS_BONUS_UNLOCKED_AT")
    ac_lucky_streak_seen: Optional[bool] = Field(None,
                                                 alias="AC_LUCKY_STREAK_SEEN")
    ac_lucky_streak_unlocked_at: Optional[int] = Field(
        None, alias="AC_LUCKY_STREAK_UNLOCKED_AT")
    ac_cryptic_streak_seen: Optional[bool] = Field(
        None, alias="AC_CRYPTIC_STREAK_SEEN")
    ac_cryptic_streak_unlocked_at: Optional[int] = Field(
        None, alias="AC_CRYPTIC_STREAK_UNLOCKED_AT")
    ac_mysterious_streak_seen: Optional[bool] = Field(
        None, alias="AC_MYSTERIOUS_STREAK_SEEN")
    ac_mysterious_streak_unlocked_at: Optional[int] = Field(
        None, alias="AC_MYSTERIOUS_STREAK_UNLOCKED_AT")
    ac_say_cheese_seen: Optional[bool] = Field(None,
                                               alias="AC_SAY_CHEESE_SEEN")
    ac_say_cheese_unlocked_at: Optional[int] = Field(
        None, alias="AC_SAY_CHEESE_UNLOCKED_AT")
    ac_yearly_report_2022_seen: Optional[bool] = Field(
        None, alias="AC_YEARLY_REPORT_2022_SEEN")
    ac_yearly_report_2022_unlocked_at: Optional[int] = Field(
        None, alias="AC_YEARLY_REPORT_2022_UNLOCKED_AT")
    ac_yearly_report_2021_seen: Optional[bool] = Field(
        None, alias="AC_YEARLY_REPORT_2021_SEEN")
    ac_yearly_report_2021_unlocked_at: Optional[int] = Field(
        None, alias="AC_YEARLY_REPORT_2021_UNLOCKED_AT")
    ac_yearly_report_2020_seen: Optional[bool] = Field(
        None, alias="AC_YEARLY_REPORT_2020_SEEN")
    ac_yearly_report_2020_unlocked_at: Optional[int] = Field(
        None, alias="AC_YEARLY_REPORT_2020_UNLOCKED_AT")
    ac_yearly_report_2019_seen: Optional[bool] = Field(
        None, alias="AC_YEARLY_REPORT_2019_SEEN")
    ac_yearly_report_2019_unlocked_at: Optional[int] = Field(
        None, alias="AC_YEARLY_REPORT_2019_UNLOCKED_AT")
    ac_yearly_report_2018_seen: Optional[bool] = Field(
        None, alias="AC_YEARLY_REPORT_2018_SEEN")
    ac_yearly_report_2018_unlocked_at: Optional[int] = Field(
        None, alias="AC_YEARLY_REPORT_2018_UNLOCKED_AT")
    ac_yearly_report_2017_seen: Optional[bool] = Field(
        None, alias="AC_YEARLY_REPORT_2017_SEEN")
    ac_yearly_report_2017_unlocked_at: Optional[int] = Field(
        None, alias="AC_YEARLY_REPORT_2017_UNLOCKED_AT")
    ac_yearly_report_2016_seen: Optional[bool] = Field(
        None, alias="AC_YEARLY_REPORT_2016_SEEN")
    ac_yearly_report_2016_unlocked_at: Optional[int] = Field(
        None, alias="AC_YEARLY_REPORT_2016_UNLOCKED_AT")


class Pref(BaseModel):
    key: str
    pref_name: str
    value: Union[int, bool, str]


class Metadatum(BaseModel):
    number_of_entries: int
    created_at: int
    is_auto_backup: bool
    platform: str
    android_version: int
    number_of_photos: int
    photos_size: int


class PreferredMoodIconsIdsForMoodIdsForIconsPack(BaseModel):
    one_: 'one_' = Field(..., alias="1")


class one_(BaseModel):
    one_: int = Field(..., alias="1")
    three_: int = Field(..., alias="3")
    two_: int = Field(..., alias="2")
    eight_: int = Field(..., alias="8")
    five_: int = Field(..., alias="5")
    four_: int = Field(..., alias="4")
    seven_: int = Field(..., alias="7")


class Reminder(BaseModel):
    id_: int = Field(..., alias="id")
    hour: int
    minute: int
    state: int
    custom_text_enabled: bool


class WritingTemplate(BaseModel):
    id_: int = Field(..., alias="id")
    order: int
    predefined_template_id: int
    title: str
    body: str


def init_pydantic() -> None:
    Daylio.update_forward_refs()
    PreferredMoodIconsIdsForMoodIdsForIconsPack.update_forward_refs()
