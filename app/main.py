from app.errors import (
    NotVaccinatedError,
    OutdatedVaccineError,
    NotWearingMaskError,
)
from app.cafe import Cafe


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    mask_amount = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (OutdatedVaccineError, NotVaccinatedError):
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_amount += 1

    if mask_amount != 0:
        return f"Friends should buy {mask_amount} masks"
    return f"Friends can go to {cafe.name}"
