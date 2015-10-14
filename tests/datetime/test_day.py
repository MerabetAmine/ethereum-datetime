import pytest

@pytest.mark.parametrize(
    'timestamp,day',
    (
        # Non leap year.
        (0, 1),
        (2678399, 31),
        (2678400, 1),
        (5097599, 28),
        (5097600, 1),
        (7775999, 31),
        (7776000, 1),
        (10367999, 30),
        (10368000, 1),
        (13046399, 31),
        (13046400, 1),
        (15638399, 30),
        (15638400, 1),
        (18316799, 31),
        (18316800, 1),
        (20995199, 31),
        (20995200, 1),
        (23587199, 30),
        (23587200, 1),
        (26265599, 31),
        (26265600, 1),
        (28857599, 30),
        (28857600, 1),
        (31535999, 31),
        (31536000, 1),

        # Leap Year
        (63071999, 31),  # Dec 31 1971
        (63072000, 1),  # Jan 1 1972
        (65750399, 31),
        (65750400, 1),  # Feb 1 1972
        (68255999, 29),
        (68256000, 1),  # Mar 1 1972
        (70934399, 31),
        (70934400, 1),  # Apr 1 1972
        (73526399, 30),
        (73526400, 1),  # May 1 1972
        (76204799, 31),
        (76204800, 1),  # Jun 1 1972
        (78796799, 30),
        (78796800, 1),  # Jul 1 1972
        (81475199, 31),
        (81475200, 1),  # Aug 1 1972
        (84153599, 31),
        (84153600, 1),  # Sep 1 1972
        (86745599, 30),
        (86745600, 1),  # Oct 1 1972
        (89423999, 31),
        (89424000, 1),  # Nov 1 1972
        (92015999, 30),
        (92016000, 1),  # Dec 1 1972
        (94694399, 31),
        (94694400, 1),  # Jan 1 1972
    ),
)
def test_get_day_from_timestamp(deployed_contracts, timestamp, day):
    crontab = deployed_contracts.DateTimeLib
    assert crontab.getDay(timestamp) == day
