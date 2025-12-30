"""
Hotel Customer Support Voice Agent Functions
Grand Horizon Hotel & Spa

This module provides all functions for the hotel customer support voice agent,
including a fake in-memory database with pre-seeded reservations for testing.
"""

import random
from datetime import datetime

# =============================================================================
# HOTEL INFORMATION DATABASE
# =============================================================================

HOTEL_INFO = {
    "name": "Grand Horizon Hotel & Spa",
    "address": "1250 Oceanview Boulevard, Marina Bay, CA 90210",
    "phone": "+1-800-555-4685",
    "email": "reservations@grandhorizonhotel.com",
    "website": "www.grandhorizonhotel.com",
    # Check-in/Check-out
    "check_in_time": "3:00 PM",
    "early_check_in": "Available from 12:00 PM for a $50 fee, subject to availability",
    "check_out_time": "11:00 AM",
    "late_check_out": "Available until 2:00 PM for a $75 fee, subject to availability",
    # Location
    "location": "Located in the heart of Marina Bay, just 15 minutes from the airport and steps away from the beach, shopping, and dining",
    "directions": "From the airport, take Highway 101 South, exit at Oceanview Boulevard, hotel is on the right",
    # Contact
    "contact": "You can reach us 24/7 at +1-800-555-4685, by email at reservations@grandhorizonhotel.com, or through our website",
    # Amenities
    "amenities": {
        "pool": "Rooftop infinity pool with panoramic ocean views, open daily 6 AM to 10 PM. Poolside bar and cabana service available",
        "gym": "24-hour fitness center featuring state-of-the-art equipment, personal trainers available by appointment",
        "spa": "Full-service Serenity Spa offering massages, facials, and body treatments. Reservations recommended, call extension 500",
        "restaurant": "Horizon Grill serves breakfast 6:30-10:30 AM, lunch 11:30 AM-2:30 PM, dinner 5:30-10 PM. Reservations recommended for dinner",
        "bar": "Skyline Lounge on the 20th floor, open 5 PM to midnight, featuring craft cocktails and stunning sunset views",
        "wifi": "Complimentary high-speed WiFi throughout the hotel. Premium bandwidth available for $15 per day",
        "parking": "Valet parking $35 per night, self-parking garage $25 per night. Electric vehicle charging stations available",
        "business_center": "24-hour business center with printing, scanning, and video conferencing facilities",
        "concierge": "24-hour concierge service for restaurant reservations, tours, and local recommendations",
        "room_service": "In-room dining available 24 hours. Full menu until 11 PM, limited menu overnight",
    },
    # Policies
    "policies": {
        "cancellation": "Free cancellation if done 48 hours or more before check-in. Cancellations within 48 hours will be charged for the first night. No-shows will be charged the full reservation amount",
        "pets": "We welcome dogs under 50 pounds with a $75 per stay pet fee. Please inform us in advance. Service animals are always welcome at no charge",
        "smoking": "Grand Horizon is a 100% non-smoking property. A $250 cleaning fee applies if smoking is detected in rooms",
        "age_requirement": "Guests must be 21 years or older to check in. Valid government-issued ID required",
        "payment": "We accept all major credit cards. A valid credit card is required at check-in for incidentals",
        "quiet_hours": "Quiet hours are from 10 PM to 8 AM to ensure all guests enjoy a peaceful stay",
    },
    # Room Types
    "room_types": {
        "standard": {
            "name": "Standard Room",
            "description": "Comfortable 325 sq ft room with one king or two queen beds, city view",
            "price_per_night": 149,
            "max_guests": 2,
        },
        "deluxe": {
            "name": "Deluxe Room",
            "description": "Spacious 425 sq ft room with ocean view, sitting area, and premium amenities",
            "price_per_night": 199,
            "max_guests": 3,
        },
        "suite": {
            "name": "Executive Suite",
            "description": "Luxurious 650 sq ft suite with separate living area, ocean view, and executive lounge access",
            "price_per_night": 349,
            "max_guests": 4,
        },
        "penthouse": {
            "name": "Penthouse Suite",
            "description": "Ultimate luxury in 1,200 sq ft with wraparound terrace, private butler service, and panoramic views",
            "price_per_night": 699,
            "max_guests": 6,
        },
    },
}

# =============================================================================
# RESERVATIONS DATABASE (Pre-seeded with test data)
# =============================================================================

RESERVATIONS_DB = {
    "reservations": {
        "GH-78432": {
            "guest_name": "John Smith",
            "last_name": "smith",  # Stored lowercase for case-insensitive matching
            "phone": "+1-555-123-4567",
            "email": "john.smith@email.com",
            "check_in": "2026-01-15",
            "check_out": "2026-01-18",
            "room_type": "deluxe",
            "room_number": "412",
            "guests": 2,
            "nights": 3,
            "rate_per_night": 199.00,
            "total_cost": 597.00,
            "status": "confirmed",
            "special_requests": ["Late check-in around 9 PM", "High floor preferred"],
            "created_at": "2024-12-20",
            "payment_status": "paid",
        },
        "GH-92156": {
            "guest_name": "Sarah Johnson",
            "last_name": "johnson",
            "phone": "+1-555-987-6543",
            "email": "sarah.j@email.com",
            "check_in": "2026-01-10",
            "check_out": "2026-01-12",
            "room_type": "suite",
            "room_number": "801",
            "guests": 4,
            "nights": 2,
            "rate_per_night": 349.00,
            "total_cost": 698.00,
            "status": "confirmed",
            "special_requests": ["Airport shuttle pickup", "Champagne upon arrival"],
            "created_at": "2024-12-15",
            "payment_status": "paid",
        },
        "GH-45891": {
            "guest_name": "Michael Chen",
            "last_name": "chen",
            "phone": "+1-555-456-7890",
            "email": "mchen@business.com",
            "check_in": "2026-01-20",
            "check_out": "2026-01-25",
            "room_type": "standard",
            "room_number": "215",
            "guests": 1,
            "nights": 5,
            "rate_per_night": 149.00,
            "total_cost": 745.00,
            "status": "confirmed",
            "special_requests": ["Early check-in if possible", "Extra pillows"],
            "created_at": "2024-12-22",
            "payment_status": "deposit_paid",
        },
        "GH-33567": {
            "guest_name": "Emily Rodriguez",
            "last_name": "rodriguez",
            "phone": "+1-555-234-5678",
            "email": "emily.r@email.com",
            "check_in": "2026-01-08",
            "check_out": "2026-01-10",
            "room_type": "deluxe",
            "room_number": "518",
            "guests": 2,
            "nights": 2,
            "rate_per_night": 199.00,
            "total_cost": 398.00,
            "status": "confirmed",
            "special_requests": ["Anniversary celebration", "Ocean view room"],
            "created_at": "2024-12-18",
            "payment_status": "paid",
        },
        "GH-67234": {
            "guest_name": "David Williams",
            "last_name": "williams",
            "phone": "+1-555-345-6789",
            "email": "d.williams@email.com",
            "check_in": "2026-02-01",
            "check_out": "2026-02-05",
            "room_type": "penthouse",
            "room_number": "2001",
            "guests": 4,
            "nights": 4,
            "rate_per_night": 699.00,
            "total_cost": 2796.00,
            "status": "confirmed",
            "special_requests": ["Private dinner on terrace", "Spa appointments for 2"],
            "created_at": "2024-12-10",
            "payment_status": "paid",
        },
        "GH-11223": {
            "guest_name": "Lisa Thompson",
            "last_name": "thompson",
            "phone": "+1-555-678-9012",
            "email": "lisa.t@email.com",
            "check_in": "2026-01-25",
            "check_out": "2026-01-27",
            "room_type": "standard",
            "room_number": "302",
            "guests": 2,
            "nights": 2,
            "rate_per_night": 149.00,
            "total_cost": 298.00,
            "status": "confirmed",
            "special_requests": ["Quiet room away from elevator"],
            "created_at": "2024-12-23",
            "payment_status": "paid",
        },
    },
    "cancelled_reservations": {},
    "callback_requests": {},
    "next_callback_id": 5001,
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


def _verify_reservation(confirmation_number: str, last_name: str) -> tuple:
    """
    Verify a reservation exists and the last name matches.
    Returns (success: bool, reservation_or_error: dict/str)
    """
    conf_num = confirmation_number.upper().strip()

    # Check if reservation exists
    if conf_num not in RESERVATIONS_DB["reservations"]:
        # Check cancelled reservations
        if conf_num in RESERVATIONS_DB["cancelled_reservations"]:
            return (False, "cancelled")
        return (False, "not_found")

    reservation = RESERVATIONS_DB["reservations"][conf_num]

    # Verify last name (case-insensitive)
    if reservation["last_name"] != last_name.lower().strip():
        return (False, "name_mismatch")

    return (True, reservation)


def _calculate_cancellation_fee(check_in_date: str) -> dict:
    """
    Calculate cancellation fee based on check-in date and policy.
    """
    check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
    now = datetime.now()
    hours_until_checkin = (check_in - now).total_seconds() / 3600

    if hours_until_checkin >= 48:
        return {
            "fee": 0,
            "refund_type": "full_refund",
            "message": "Your cancellation is more than 48 hours before check-in. You will receive a full refund.",
        }
    elif hours_until_checkin > 0:
        return {
            "fee": "first_night",
            "refund_type": "partial_refund",
            "message": "Your cancellation is within 48 hours of check-in. The first night will be charged as per our cancellation policy.",
        }
    else:
        return {
            "fee": "full_amount",
            "refund_type": "no_refund",
            "message": "The check-in date has passed. Unfortunately, no refund is available for this reservation.",
        }


def _generate_callback_id() -> str:
    """Generate a unique callback reference number."""
    callback_id = f"CB-{RESERVATIONS_DB['next_callback_id']}"
    RESERVATIONS_DB["next_callback_id"] += 1
    return callback_id


# =============================================================================
# MAIN FUNCTIONS (Called by Voice Agent)
# =============================================================================


def get_hotel_info(category: str) -> dict:
    """
    Get hotel information for a specific category.

    Args:
        category: The type of information requested. Options:
            - 'amenities' (or specific: 'pool', 'gym', 'spa', 'restaurant', 'bar', 'wifi', 'parking')
            - 'check_in_time', 'check_out_time', 'early_check_in', 'late_check_out'
            - 'cancellation_policy', 'pet_policy', 'smoking_policy'
            - 'location', 'directions', 'contact'
            - 'room_types'

    Returns:
        dict: The requested information
    """
    category = category.lower().strip().replace(" ", "_")

    # Direct hotel info fields
    direct_fields = [
        "name",
        "address",
        "phone",
        "email",
        "website",
        "check_in_time",
        "early_check_in",
        "check_out_time",
        "late_check_out",
        "location",
        "directions",
        "contact",
    ]

    if category in direct_fields:
        return {"category": category, "information": HOTEL_INFO[category]}

    # Amenity-specific queries
    if category in HOTEL_INFO["amenities"]:
        return {"category": category, "information": HOTEL_INFO["amenities"][category]}

    # All amenities
    if category == "amenities" or category == "all_amenities":
        amenities_list = []
        for name, description in HOTEL_INFO["amenities"].items():
            amenities_list.append(f"{name.title()}: {description}")
        return {
            "category": "amenities",
            "information": "Our hotel amenities include: " + "; ".join(amenities_list),
        }

    # Policy queries
    policy_mapping = {
        "cancellation_policy": "cancellation",
        "cancellation": "cancellation",
        "pet_policy": "pets",
        "pets": "pets",
        "smoking_policy": "smoking",
        "smoking": "smoking",
        "age_requirement": "age_requirement",
        "payment": "payment",
        "quiet_hours": "quiet_hours",
    }

    if category in policy_mapping:
        policy_key = policy_mapping[category]
        return {"category": category, "information": HOTEL_INFO["policies"][policy_key]}

    # Room types
    if category == "room_types" or category == "rooms":
        room_info = []
        for room_key, room_data in HOTEL_INFO["room_types"].items():
            room_info.append(
                f"{room_data['name']} - ${room_data['price_per_night']} per night, "
                f"up to {room_data['max_guests']} guests. {room_data['description']}"
            )
        return {
            "category": "room_types",
            "information": "We offer the following room types: "
            + " | ".join(room_info),
        }

    # Unknown category
    return {
        "category": category,
        "error": f"I don't have specific information for '{category}'. I can help you with: amenities, check-in/check-out times, policies (cancellation, pets, smoking), location, directions, contact information, or room types. What would you like to know?",
    }


def lookup_reservation(confirmation_number: str, last_name: str) -> dict:
    """
    Look up a reservation by confirmation number and verify with last name.

    Args:
        confirmation_number: The reservation confirmation number (e.g., 'GH-78432')
        last_name: Guest's last name for verification

    Returns:
        dict: Reservation details or error message
    """
    success, result = _verify_reservation(confirmation_number, last_name)

    if not success:
        if result == "not_found":
            return {
                "error": "reservation_not_found",
                "message": f"I couldn't find a reservation with confirmation number {confirmation_number.upper()}. Please double-check the number. It should start with 'GH-' followed by 5 digits.",
            }
        elif result == "cancelled":
            cancelled = RESERVATIONS_DB["cancelled_reservations"].get(
                confirmation_number.upper(), {}
            )
            return {
                "error": "reservation_cancelled",
                "message": f"This reservation was cancelled on {cancelled.get('cancelled_on', 'a previous date')}. Cancellation reference: {cancelled.get('cancellation_ref', 'N/A')}.",
            }
        elif result == "name_mismatch":
            return {
                "error": "verification_failed",
                "message": "I found the reservation, but the last name provided doesn't match our records. For security, I cannot share the reservation details. Please verify you have the correct last name.",
            }

    # Success - return reservation details
    reservation = result
    room_type_info = HOTEL_INFO["room_types"].get(reservation["room_type"], {})

    return {
        "status": "found",
        "confirmation_number": confirmation_number.upper(),
        "guest_name": reservation["guest_name"],
        "check_in_date": reservation["check_in"],
        "check_out_date": reservation["check_out"],
        "nights": reservation["nights"],
        "room_type": room_type_info.get("name", reservation["room_type"]),
        "room_number": reservation["room_number"],
        "number_of_guests": reservation["guests"],
        "rate_per_night": f"${reservation['rate_per_night']:.2f}",
        "total_cost": f"${reservation['total_cost']:.2f}",
        "reservation_status": reservation["status"],
        "payment_status": reservation["payment_status"],
        "special_requests": reservation["special_requests"],
        "message": f"I found your reservation, {reservation['guest_name']}. You have a {room_type_info.get('name', reservation['room_type'])} booked for {reservation['nights']} nights, checking in on {reservation['check_in']} and checking out on {reservation['check_out']}. Your room number is {reservation['room_number']} and the total cost is ${reservation['total_cost']:.2f}.",
    }


def cancel_reservation(
    confirmation_number: str, last_name: str, cancellation_reason: str
) -> dict:
    """
    Cancel a reservation after verification.

    Args:
        confirmation_number: The reservation confirmation number
        last_name: Guest's last name for verification
        cancellation_reason: Reason for cancellation (change_of_plans, emergency,
                           found_alternative, price_concern, other)

    Returns:
        dict: Cancellation confirmation or error
    """
    success, result = _verify_reservation(confirmation_number, last_name)

    if not success:
        if result == "not_found":
            return {
                "error": "reservation_not_found",
                "message": f"I couldn't find a reservation with confirmation number {confirmation_number.upper()}. Please verify the confirmation number is correct.",
            }
        elif result == "cancelled":
            return {
                "error": "already_cancelled",
                "message": "This reservation has already been cancelled. No further action is needed.",
            }
        elif result == "name_mismatch":
            return {
                "error": "verification_failed",
                "message": "The last name provided doesn't match our records. For security purposes, I cannot process this cancellation. Please verify you have the correct information.",
            }

    reservation = result
    conf_num = confirmation_number.upper().strip()

    # Calculate cancellation fee
    fee_info = _calculate_cancellation_fee(reservation["check_in"])

    # Generate cancellation reference
    cancellation_ref = f"CXL-{conf_num}-{datetime.now().strftime('%Y%m%d')}"

    # Process cancellation
    cancelled_reservation = {
        **reservation,
        "cancelled_on": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "cancellation_reason": cancellation_reason,
        "cancellation_ref": cancellation_ref,
        "cancellation_fee": fee_info["fee"],
        "refund_type": fee_info["refund_type"],
    }

    # Move to cancelled reservations
    RESERVATIONS_DB["cancelled_reservations"][conf_num] = cancelled_reservation
    del RESERVATIONS_DB["reservations"][conf_num]

    # Prepare response based on refund type
    if fee_info["refund_type"] == "full_refund":
        refund_message = f"A full refund of ${reservation['total_cost']:.2f} will be processed to your original payment method within 5-7 business days."
    elif fee_info["refund_type"] == "partial_refund":
        refund_amount = reservation["total_cost"] - reservation["rate_per_night"]
        refund_message = f"As per our cancellation policy, the first night (${reservation['rate_per_night']:.2f}) will be charged. A refund of ${refund_amount:.2f} will be processed within 5-7 business days."
    else:
        refund_message = "As the check-in date has passed, no refund is available for this reservation."

    return {
        "status": "cancelled",
        "cancellation_reference": cancellation_ref,
        "original_confirmation": conf_num,
        "guest_name": reservation["guest_name"],
        "check_in_date": reservation["check_in"],
        "check_out_date": reservation["check_out"],
        "cancellation_policy_applied": fee_info["message"],
        "refund_information": refund_message,
        "message": f"Your reservation has been successfully cancelled. Your cancellation reference number is {cancellation_ref}. Please save this for your records. {refund_message}",
    }


def modify_reservation(
    confirmation_number: str, last_name: str, modification_type: str, new_value: str
) -> dict:
    """
    Modify an existing reservation.

    Args:
        confirmation_number: The reservation confirmation number
        last_name: Guest's last name for verification
        modification_type: Type of modification (check_in_date, check_out_date,
                          room_type, guest_count, add_request)
        new_value: The new value for the modification

    Returns:
        dict: Modification confirmation or error
    """
    success, result = _verify_reservation(confirmation_number, last_name)

    if not success:
        if result == "not_found":
            return {
                "error": "reservation_not_found",
                "message": f"I couldn't find a reservation with confirmation number {confirmation_number.upper()}.",
            }
        elif result == "cancelled":
            return {
                "error": "reservation_cancelled",
                "message": "This reservation has been cancelled and cannot be modified. Would you like me to help you make a new reservation?",
            }
        elif result == "name_mismatch":
            return {
                "error": "verification_failed",
                "message": "The last name provided doesn't match our records. I cannot process this modification.",
            }

    reservation = result
    conf_num = confirmation_number.upper().strip()
    modification_type = modification_type.lower().strip()

    # Store original values for comparison
    original_total = reservation["total_cost"]
    changes_made = []

    if modification_type == "check_in_date":
        try:
            new_date = datetime.strptime(new_value, "%Y-%m-%d")
            old_date = reservation["check_in"]
            reservation["check_in"] = new_value

            # Recalculate nights and total
            check_out = datetime.strptime(reservation["check_out"], "%Y-%m-%d")
            nights = (check_out - new_date).days
            if nights <= 0:
                reservation["check_in"] = old_date  # Revert
                return {
                    "error": "invalid_dates",
                    "message": "The new check-in date must be before the check-out date. Please provide a valid date.",
                }

            reservation["nights"] = nights
            reservation["total_cost"] = nights * reservation["rate_per_night"]
            changes_made.append(f"Check-in date changed from {old_date} to {new_value}")

        except ValueError:
            return {
                "error": "invalid_date_format",
                "message": "Please provide the date in YYYY-MM-DD format, for example 2025-01-15.",
            }

    elif modification_type == "check_out_date":
        try:
            new_date = datetime.strptime(new_value, "%Y-%m-%d")
            old_date = reservation["check_out"]
            check_in = datetime.strptime(reservation["check_in"], "%Y-%m-%d")
            nights = (new_date - check_in).days

            if nights <= 0:
                return {
                    "error": "invalid_dates",
                    "message": "The check-out date must be after the check-in date. Please provide a valid date.",
                }

            reservation["check_out"] = new_value
            reservation["nights"] = nights
            reservation["total_cost"] = nights * reservation["rate_per_night"]
            changes_made.append(
                f"Check-out date changed from {old_date} to {new_value}"
            )

        except ValueError:
            return {
                "error": "invalid_date_format",
                "message": "Please provide the date in YYYY-MM-DD format, for example 2025-01-18.",
            }

    elif modification_type == "room_type":
        new_room = new_value.lower().strip()
        if new_room not in HOTEL_INFO["room_types"]:
            available = ", ".join(
                [r["name"] for r in HOTEL_INFO["room_types"].values()]
            )
            return {
                "error": "invalid_room_type",
                "message": f"'{new_value}' is not a valid room type. Available options are: {available}.",
            }

        old_room = reservation["room_type"]
        old_room_name = HOTEL_INFO["room_types"][old_room]["name"]
        new_room_info = HOTEL_INFO["room_types"][new_room]

        # Check guest capacity
        if reservation["guests"] > new_room_info["max_guests"]:
            return {
                "error": "capacity_exceeded",
                "message": f"The {new_room_info['name']} has a maximum capacity of {new_room_info['max_guests']} guests, but your reservation is for {reservation['guests']} guests. Please choose a larger room type or reduce the number of guests.",
            }

        reservation["room_type"] = new_room
        reservation["rate_per_night"] = new_room_info["price_per_night"]
        reservation["total_cost"] = (
            reservation["nights"] * new_room_info["price_per_night"]
        )
        changes_made.append(
            f"Room type changed from {old_room_name} to {new_room_info['name']}"
        )

    elif modification_type == "guest_count":
        try:
            new_guests = int(new_value)
            room_info = HOTEL_INFO["room_types"][reservation["room_type"]]

            if new_guests <= 0:
                return {
                    "error": "invalid_guest_count",
                    "message": "The number of guests must be at least 1.",
                }

            if new_guests > room_info["max_guests"]:
                return {
                    "error": "capacity_exceeded",
                    "message": f"Your current room ({room_info['name']}) has a maximum capacity of {room_info['max_guests']} guests. Would you like to upgrade to a larger room type?",
                }

            old_guests = reservation["guests"]
            reservation["guests"] = new_guests
            changes_made.append(
                f"Number of guests changed from {old_guests} to {new_guests}"
            )

        except ValueError:
            return {
                "error": "invalid_guest_count",
                "message": "Please provide a valid number for the guest count.",
            }

    elif modification_type == "add_request":
        reservation["special_requests"].append(new_value)
        changes_made.append(f"Added special request: {new_value}")

    else:
        return {
            "error": "invalid_modification_type",
            "message": "I can help you modify: check-in date, check-out date, room type, guest count, or add a special request. What would you like to change?",
        }

    # Calculate price difference
    price_difference = reservation["total_cost"] - original_total

    if price_difference > 0:
        price_message = f"This change results in an additional charge of ${price_difference:.2f}. Your new total is ${reservation['total_cost']:.2f}."
    elif price_difference < 0:
        price_message = f"This change results in a credit of ${abs(price_difference):.2f}. Your new total is ${reservation['total_cost']:.2f}."
    else:
        price_message = f"Your total remains ${reservation['total_cost']:.2f}."

    return {
        "status": "modified",
        "confirmation_number": conf_num,
        "changes_made": changes_made,
        "new_check_in": reservation["check_in"],
        "new_check_out": reservation["check_out"],
        "new_room_type": HOTEL_INFO["room_types"][reservation["room_type"]]["name"],
        "new_guest_count": reservation["guests"],
        "new_total": f"${reservation['total_cost']:.2f}",
        "price_difference": f"${price_difference:.2f}"
        if price_difference != 0
        else "No change",
        "special_requests": reservation["special_requests"],
        "message": f"Your reservation has been updated. {'; '.join(changes_made)}. {price_message}",
    }


def request_callback(
    guest_name: str, phone_number: str, issue_description: str
) -> dict:
    """
    Request a callback from a human agent for complex issues.

    Args:
        guest_name: Name of the guest requesting callback
        phone_number: Phone number to call back
        issue_description: Brief description of the issue

    Returns:
        dict: Callback request confirmation
    """
    callback_id = _generate_callback_id()

    # Store callback request
    RESERVATIONS_DB["callback_requests"][callback_id] = {
        "guest_name": guest_name,
        "phone_number": phone_number,
        "issue_description": issue_description,
        "requested_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "status": "pending",
    }

    # Estimate wait time based on "queue" (random for demo)
    estimated_wait = random.choice([15, 30, 45, 60])

    return {
        "status": "callback_scheduled",
        "callback_reference": callback_id,
        "guest_name": guest_name,
        "phone_number": phone_number,
        "estimated_callback_time": f"Within {estimated_wait} minutes",
        "message": f"Thank you, {guest_name}. I've submitted a callback request with reference number {callback_id}. A member of our guest services team will call you at {phone_number} within {estimated_wait} minutes. Is there anything else I can help you with in the meantime?",
    }


# =============================================================================
# FUNCTION MAPPING (Used by voice agent)
# =============================================================================

FUNCTION_MAP = {
    "get_hotel_info": get_hotel_info,
    "lookup_reservation": lookup_reservation,
    "cancel_reservation": cancel_reservation,
    "modify_reservation": modify_reservation,
    "request_callback": request_callback,
}
