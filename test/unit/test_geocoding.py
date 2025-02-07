"""Test suite for dbcp.transform.geocoding module."""
import pytest

from dbcp.transform.geocoding import GoogleGeocoder


class mock_geocoder(GoogleGeocoder):
    """Mock GoogleGeocoder class for testing."""

    def __init__(
        self, request_kwargs: dict[str, str], response: dict[str, list[dict[str, str]]]
    ) -> None:
        """Initialize mock geocoder."""
        # overwrite __init__ to skip over API client creation
        self._clear_cache()  # initialize attributes

        # mock gc.geocode_request(**request_kwargs)
        if request_kwargs.get("country", None) is None:
            request_kwargs["country"] = "US"
        self._name = request_kwargs["name"]
        self._state = request_kwargs["state"]
        self._country = request_kwargs["country"]
        self._response = response
        return


def mock_geocoder_street_address() -> GoogleGeocoder:
    """An edge case where the geocoder returns a street address of the town hall."""
    request_kwargs = dict(
        name="Town of Seneca (Ontario County)", state="NY", country="US"
    )
    resp = {
        "address_components": [
            {"long_name": "3675", "short_name": "3675", "types": ["street_number"]},
            {"long_name": "Flint Road", "short_name": "Flint Rd", "types": ["route"]},
            {
                "long_name": "Stanley",
                "short_name": "Stanley",
                "types": ["locality", "political"],
            },
            {
                "long_name": "Seneca",
                "short_name": "Seneca",
                "types": ["administrative_area_level_3", "political"],
            },
            {
                "long_name": "Ontario County",
                "short_name": "Ontario County",
                "types": ["administrative_area_level_2", "political"],
            },
            {
                "long_name": "New York",
                "short_name": "NY",
                "types": ["administrative_area_level_1", "political"],
            },
            {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"],
            },
            {"long_name": "14561", "short_name": "14561", "types": ["postal_code"]},
            {
                "long_name": "9575",
                "short_name": "9575",
                "types": ["postal_code_suffix"],
            },
        ],
        "formatted_address": "3675 Flint Rd, Stanley, NY 14561, USA",
        # truncated ...
        "partial_match": True,
        "types": ["establishment", "local_government_office", "point_of_interest"],
    }
    return mock_geocoder(request_kwargs, resp)


def mock_geocoder_town_and_county() -> GoogleGeocoder:
    """A typical geocoder request for RELDI local opposition data."""
    request_kwargs = dict(
        name="Town of Westport (Dane County)", state="WI", country="US"
    )
    resp = {
        "address_components": [
            {
                "long_name": "Westport",
                "short_name": "Westport",
                "types": ["locality", "political"],
            },
            {
                "long_name": "Mary Lake",
                "short_name": "Mary Lake",
                "types": ["neighborhood", "political"],
            },
            {
                "long_name": "Westport",
                "short_name": "Westport",
                "types": ["administrative_area_level_3", "political"],
            },
            {
                "long_name": "Dane County",
                "short_name": "Dane County",
                "types": ["administrative_area_level_2", "political"],
            },
            {
                "long_name": "Wisconsin",
                "short_name": "WI",
                "types": ["administrative_area_level_1", "political"],
            },
            {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"],
            },
            {"long_name": "53597", "short_name": "53597", "types": ["postal_code"]},
        ],
        "formatted_address": "Westport, WI 53597, USA",
        # truncated ...
        "place_id": "ChIJRZO585GqB4gRZ-Wtajrhvo4",
        "types": ["locality", "political"],
    }
    return mock_geocoder(request_kwargs, resp)


def mock_geocoder_county() -> GoogleGeocoder:
    """A typical geocoder request for ISO queue data.

    There is a name collision between a town and its containing county of the same name.
    """
    request_kwargs = dict(name="new madrid", state="MO", country="US")
    resp = {
        "address_components": [
            {
                "long_name": "New Madrid",
                "short_name": "New Madrid",
                "types": ["locality", "political"],
            },
            {
                "long_name": "New Madrid Township",
                "short_name": "New Madrid Township",
                "types": ["administrative_area_level_3", "political"],
            },
            {
                "long_name": "New Madrid County",
                "short_name": "New Madrid County",
                "types": ["administrative_area_level_2", "political"],
            },
            {
                "long_name": "Missouri",
                "short_name": "MO",
                "types": ["administrative_area_level_1", "political"],
            },
            {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"],
            },
            {"long_name": "63869", "short_name": "63869", "types": ["postal_code"]},
        ],
        "formatted_address": "New Madrid, MO 63869, USA",
        # truncated ...
        "place_id": "ChIJ_64qVYr3eIgRLLQnMg1825Y",
        "types": ["locality", "political"],
    }
    return mock_geocoder(request_kwargs, resp)


def mock_geocoder_county_explicit() -> GoogleGeocoder:
    """A typical geocoder request for offshore wind data.

    The full county name is explicitly provided
    """
    request_kwargs = dict(name="new madrid county", state="MO", country="US")
    resp = {
        "address_components": [
            {
                "long_name": "New Madrid County",
                "short_name": "New Madrid County",
                "types": ["administrative_area_level_2", "political"],
            },
            {
                "long_name": "Missouri",
                "short_name": "MO",
                "types": ["administrative_area_level_1", "political"],
            },
            {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"],
            },
        ],
        "formatted_address": "New Madrid County, MO, USA",
        # truncated ...
        "types": ["administrative_area_level_2", "political"],
    }
    return mock_geocoder(request_kwargs, resp)


def mock_geocoder_independent_city() -> GoogleGeocoder:
    """A typical geocoder request for an independent city (no county)."""
    request_kwargs = dict(name="city of hampton", state="va", country="US")
    resp = {
        "address_components": [
            {
                "long_name": "Hampton",
                "short_name": "Hampton",
                "types": ["locality", "political"],
            },
            {
                "long_name": "Virginia",
                "short_name": "VA",
                "types": ["administrative_area_level_1", "political"],
            },
            {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"],
            },
        ],
        "formatted_address": "Hampton, VA, USA",
        # truncated ...
        "place_id": "ChIJ7ZVLmwGFuokRXXOEtSJCVkw",
        "types": ["locality", "political"],
    }
    return mock_geocoder(request_kwargs, resp)


@pytest.mark.parametrize(
    "geocoder,expected",
    [
        (
            mock_geocoder_street_address(),
            {
                "locality_name": "Seneca",
                "containing_county": "Ontario County",
                "admin_type": "city",
            },
        ),
        (
            mock_geocoder_town_and_county(),
            {
                "locality_name": "Westport",
                "containing_county": "Dane County",
                "admin_type": "city",
            },
        ),
        (
            mock_geocoder_county(),
            {
                "locality_name": "New Madrid",
                "containing_county": "New Madrid County",
                "admin_type": "city",
            },
        ),
        (
            mock_geocoder_county_explicit(),
            {
                "locality_name": "New Madrid County",
                "containing_county": "New Madrid County",
                "admin_type": "county",
            },
        ),
        (
            mock_geocoder_independent_city(),
            {
                "locality_name": "Hampton",
                "containing_county": "Hampton",
                "admin_type": "city",
            },
        ),
    ],
)
def test_geocode_locality(geocoder, expected):
    """Test the geocoder parsers."""
    # The following commented code is for debugging. Remove the @property decorator
    # on locality_name() to use it.

    # def test_geocode_locality():
    #     geocoder = mock_geocoder_town_and_county()
    #     expected = {
    #         "locality_name": "Westport",
    #         "containing_county": "Dane County",
    #         "admin_type": "city",
    #     }
    assert geocoder.locality_name == expected["locality_name"]
    assert geocoder.containing_county == expected["containing_county"]
    assert geocoder.admin_type == expected["admin_type"]


def test_GoogleGeocoder_init_and_properties():
    """Test the init and @property decorators."""
    empty = GoogleGeocoder()
    with pytest.raises(AttributeError) as e:
        empty.locality_name
        assert str(e).endswith("Call geocode_request() first.")
    full = GoogleGeocoder()
    full._response = mock_geocoder_town_and_county()._response
    assert full.locality_name == "Westport"
