# ownership_systems.py
# Lightweight fictional ownership and servitude systems module for WorldCore.
# This is clean worldbuilding data only. It does not describe graphic abuse.

ownership_systems = {
    "forced_slavery": {
        "display_name": "Forced Slavery",
        "system_type": "forced",
        "coercive_level": "extreme",
        "legal_status": "legal_in_oppressive_regions",
        "common_regions": ["old_empire_zone", "underground_black_market"],
        "entry_methods": ["capture", "illegal_sale", "inherited_status"],
        "exit_methods": ["manumission", "escape", "legal_rescue", "abolition_order"],
        "controlling_groups": ["old_empire_houses", "black_market_brokers"],
        "protections": ["rare_local_limits", "anti_slavery_rescue_laws"],
        "restrictions": ["movement_restricted", "contract_rights_denied"],
        "public_opinion": "feared_and_condemned_by_free_regions",
        "notes": "An oppressive forced system treated as a major injustice in the lore."
    },
    "debt_bondage": {
        "display_name": "Debt Bondage",
        "system_type": "forced_or_coerced",
        "coercive_level": "high",
        "legal_status": "regulated_or_abused_by_region",
        "common_regions": ["corporate_city_region", "old_empire_zone"],
        "entry_methods": ["unpaid_debt", "family_debt", "predatory_contract"],
        "exit_methods": ["debt_paid", "court_release", "debt_forgiveness"],
        "controlling_groups": ["credit_houses", "corporate_courts"],
        "protections": ["term_limits_in_some_regions", "debt_review_courts"],
        "restrictions": ["work_assignment", "travel_limits"],
        "public_opinion": "controversial",
        "notes": "Often presented as legal debt service, but easily becomes coercive."
    },
    "war_captive_servitude": {
        "display_name": "War Captive Servitude",
        "system_type": "forced",
        "coercive_level": "high",
        "legal_status": "wartime_exception_in_some_states",
        "common_regions": ["old_empire_zone", "demon_realm_borderlands"],
        "entry_methods": ["battle_capture", "occupation_law"],
        "exit_methods": ["prisoner_exchange", "peace_treaty", "asylum"],
        "controlling_groups": ["military_commands", "border_legions"],
        "protections": ["prisoner_codes", "neutral_inspection"],
        "restrictions": ["movement_restricted", "assigned_labor"],
        "public_opinion": "accepted_by_hardline_states_but_opposed_by_free_cities",
        "notes": "A coercive wartime system with frequent political conflict."
    },
    "criminal_punishment_servitude": {
        "display_name": "Criminal Punishment Servitude",
        "system_type": "penal",
        "coercive_level": "medium_to_high",
        "legal_status": "legal_in_some_regions",
        "common_regions": ["royal_capital_district", "old_empire_zone"],
        "entry_methods": ["court_sentence", "royal_decree"],
        "exit_methods": ["sentence_completed", "appeal", "pardon"],
        "controlling_groups": ["courts", "wardens", "royal_offices"],
        "protections": ["sentence_records", "appeal_process"],
        "restrictions": ["assigned_duty", "supervised_movement"],
        "public_opinion": "depends_on_fairness_of_courts",
        "notes": "Can be lawful punishment or abused by corrupt authorities."
    },
    "magical_contract_servitude": {
        "display_name": "Magical Contract Servitude",
        "system_type": "contract",
        "coercive_level": "variable",
        "legal_status": "regulated_in_magic_regions",
        "common_regions": ["magic_contract_province"],
        "entry_methods": ["signed_oath", "curse_contract", "service_pact"],
        "exit_methods": ["contract_completed", "contract_broken_by_court", "release_ritual"],
        "controlling_groups": ["contract_mages", "arcane_courts"],
        "protections": ["consent_review", "contract_registry"],
        "restrictions": ["oath_terms", "magic_limits"],
        "public_opinion": "accepted_when_voluntary_condemned_when_forced",
        "notes": "Magical contracts range from fair service pacts to coercive binding."
    },
    "corporate_ownership": {
        "display_name": "Corporate Ownership",
        "system_type": "corporate_control",
        "coercive_level": "high",
        "legal_status": "legal_in_corporate_zones",
        "common_regions": ["corporate_city_region"],
        "entry_methods": ["employment_debt", "citizenship_contract", "asset_status"],
        "exit_methods": ["contract_buyout", "labor_court", "free_city_asylum"],
        "controlling_groups": ["megacorporations", "private_security"],
        "protections": ["worker_codes_on_paper", "audit_boards"],
        "restrictions": ["housing_control", "job_assignment", "identity_limits"],
        "public_opinion": "marketed_as_order_but_seen_as_oppressive_by_critics",
        "notes": "Corporate law turns people into controlled labor assets in harsh regions."
    },
    "royal_household_servitude": {
        "display_name": "Royal Household Servitude",
        "system_type": "household_service",
        "coercive_level": "variable",
        "legal_status": "traditional_and_regulated",
        "common_regions": ["royal_capital_district"],
        "entry_methods": ["household_contract", "family_service_line", "court_assignment"],
        "exit_methods": ["retirement", "release_letter", "royal_pardon"],
        "controlling_groups": ["royal_households", "palace_stewards"],
        "protections": ["household_codes", "court_petition"],
        "restrictions": ["protocol_rules", "residence_limits"],
        "public_opinion": "prestigious_when_voluntary_criticized_when_forced",
        "notes": "Can be respected service or coercive depending on local law."
    },
    "military_servitude": {
        "display_name": "Military Servitude",
        "system_type": "military_service",
        "coercive_level": "medium_to_high",
        "legal_status": "state_controlled",
        "common_regions": ["demon_realm_borderlands", "old_empire_zone"],
        "entry_methods": ["draft", "sentence_conversion", "oath_service"],
        "exit_methods": ["term_completed", "medical_release", "command_pardon"],
        "controlling_groups": ["military_commands", "border_orders"],
        "protections": ["service_codes", "rank_review"],
        "restrictions": ["deployment_orders", "chain_of_command"],
        "public_opinion": "respected_when_fair_feared_when_forced",
        "notes": "May be duty, punishment, or coercion depending on region."
    },
    "arena_combat_servitude": {
        "display_name": "Arena Combat Servitude",
        "system_type": "forced_entertainment_labor",
        "coercive_level": "high",
        "legal_status": "banned_in_free_regions",
        "common_regions": ["underground_black_market", "old_empire_zone"],
        "entry_methods": ["capture", "criminal_sentence", "debt_transfer"],
        "exit_methods": ["freedom_prize", "legal_rescue", "ban_enforcement"],
        "controlling_groups": ["arena_masters", "black_market_sponsors"],
        "protections": ["limited_rules_in_legal_arenas"],
        "restrictions": ["movement_restricted", "combat_assignment"],
        "public_opinion": "popular_in_cruel_regions_condemned_elsewhere",
        "notes": "A coercive spectacle system opposed by reformers and free cities."
    },
    "divine_servitude": {
        "display_name": "Divine Servitude",
        "system_type": "religious_service",
        "coercive_level": "variable",
        "legal_status": "temple_law",
        "common_regions": ["divine_temple_state"],
        "entry_methods": ["vow", "temple_sentence", "chosen_service"],
        "exit_methods": ["vow_completed", "temple_release", "doctrine_review"],
        "controlling_groups": ["temple_orders", "divine_courts"],
        "protections": ["sacred_codes", "vow_review"],
        "restrictions": ["temple_rules", "ritual_duties"],
        "public_opinion": "honored_when_voluntary_questioned_when_forced",
        "notes": "Religious service can be sincere devotion or coercive temple control."
    },
    "voluntary_bonded_devotion": {
        "display_name": "Voluntary Bonded Devotion",
        "system_type": "voluntary",
        "coercive_level": "none_when_valid",
        "legal_status": "legal_with_consent_rules",
        "common_regions": ["free_city_alliance", "divine_temple_state"],
        "entry_methods": ["clear_consent", "renewable_vow", "service_oath"],
        "exit_methods": ["revocation_period", "term_end", "mutual_release"],
        "controlling_groups": ["vow_registries", "free_city_courts"],
        "protections": ["consent_required", "exit_rights", "abuse_review"],
        "restrictions": ["agreed_duties_only"],
        "public_opinion": "accepted_when_consent_and_exit_rights_are_real",
        "notes": "Separated from forced systems. Valid only with clear consent and exit paths."
    },
    "slave_markets_and_auctions": {
        "display_name": "Slave Markets and Auctions",
        "system_type": "market",
        "coercive_level": "extreme",
        "legal_status": "illegal_or_restricted_in_most_regions",
        "common_regions": ["underground_black_market", "old_empire_zone"],
        "entry_methods": ["illegal_trade", "war_capture_transfer", "debt_sale"],
        "exit_methods": ["raid_rescue", "market_ban", "freedom_purchase"],
        "controlling_groups": ["black_market_brokers", "corrupt_houses"],
        "protections": ["rare_inspection", "anti_trafficking_laws"],
        "restrictions": ["identity_control", "movement_restricted"],
        "public_opinion": "widely_condemned_outside_oppressive_regions",
        "notes": "A coercive trade system targeted by anti-slavery factions."
    },
    "escape_and_freedom_laws": {
        "display_name": "Escape and Freedom Laws",
        "system_type": "freedom_law",
        "coercive_level": "protective",
        "legal_status": "active_in_free_regions",
        "common_regions": ["free_city_alliance", "royal_capital_district"],
        "entry_methods": ["asylum_claim", "freedom_petition", "rescue_registration"],
        "exit_methods": ["free_status_confirmed", "new_citizenship"],
        "controlling_groups": ["free_city_courts", "abolition_watch"],
        "protections": ["safe_harbor", "identity_restoration", "contract_review"],
        "restrictions": ["proof_review", "temporary_safehouse_rules"],
        "public_opinion": "supported_by_free_regions_opposed_by_slave_states",
        "notes": "Laws that help people exit coercive systems and regain legal status."
    },
    "anti_slavery_factions": {
        "display_name": "Anti-Slavery Factions",
        "system_type": "resistance_network",
        "coercive_level": "protective",
        "legal_status": "legal_or_outlawed_by_region",
        "common_regions": ["free_city_alliance", "demon_realm_borderlands"],
        "entry_methods": ["volunteer_membership", "refugee_contact", "rescue_alliance"],
        "exit_methods": ["retirement", "safe_transfer"],
        "controlling_groups": ["abolition_watch", "safehouse_networks"],
        "protections": ["safe_routes", "legal_aid", "status_restoration"],
        "restrictions": ["secrecy_rules", "risk_controls"],
        "public_opinion": "heroes_in_free_regions_criminalized_by_oppressive_states",
        "notes": "Groups working to end coercive systems and protect escapees."
    },
    "regional_exceptions": {
        "display_name": "Regional Exceptions",
        "system_type": "law_variant",
        "coercive_level": "variable",
        "legal_status": "varies_by_region",
        "common_regions": ["all_regions"],
        "entry_methods": ["local_law", "treaty_clause", "emergency_order"],
        "exit_methods": ["appeal", "treaty_review", "regional_reform"],
        "controlling_groups": ["local_governors", "regional_courts"],
        "protections": ["case_by_case_review"],
        "restrictions": ["local_customs", "regional_limits"],
        "public_opinion": "uncertain_and_region_dependent",
        "notes": "Tracks exceptions so laws can vary without changing the whole setting."
    }
}


regional_ownership_laws = {
    "old_empire_zone": {
        "display_name": "Old Empire Zone",
        "world_id": "old_empire",
        "legal_status": "forced_systems_legal",
        "primary_systems": ["forced_slavery", "war_captive_servitude", "arena_combat_servitude"],
        "enforcement_groups": ["imperial_houses", "legion_courts"],
        "freedom_options": ["rare_manumission", "abolition_treaty", "escape_to_free_city"],
        "banned_practices": ["unauthorized_escape_aid"],
        "public_opinion": "traditionalists_support_reformers_oppose",
        "risk_level": "very_high",
        "notes": "Oppressive region with entrenched ownership laws and reform pressure."
    },
    "corporate_city_region": {
        "display_name": "Corporate City Region",
        "world_id": "corporate_city",
        "legal_status": "corporate_control_legal",
        "primary_systems": ["debt_bondage", "corporate_ownership"],
        "enforcement_groups": ["private_security", "contract_courts"],
        "freedom_options": ["contract_buyout", "labor_court", "free_city_asylum"],
        "banned_practices": ["unregistered_person_trade"],
        "public_opinion": "marketed_as_order_but_heavily_disputed",
        "risk_level": "high",
        "notes": "Uses contracts and debt to control workers under corporate law."
    },
    "demon_realm_borderlands": {
        "display_name": "Demon Realm Borderlands",
        "world_id": "demon_border",
        "legal_status": "unstable_mixed_law",
        "primary_systems": ["war_captive_servitude", "military_servitude", "anti_slavery_factions"],
        "enforcement_groups": ["border_legions", "local_warlords"],
        "freedom_options": ["safehouse_routes", "prisoner_exchange", "free_city_transfer"],
        "banned_practices": ["treaty_protected_captive_trade"],
        "public_opinion": "divided_by_survival_politics",
        "risk_level": "high",
        "notes": "Border conflict creates coercive risks and rescue networks."
    },
    "royal_capital_district": {
        "display_name": "Royal Capital District",
        "world_id": "royal_capital",
        "legal_status": "regulated_service_law",
        "primary_systems": ["royal_household_servitude", "criminal_punishment_servitude"],
        "enforcement_groups": ["royal_courts", "palace_stewards"],
        "freedom_options": ["appeal", "release_letter", "royal_pardon"],
        "banned_practices": ["unregistered_forced_sale", "black_market_transfer"],
        "public_opinion": "supports_order_but_accepts_reform",
        "risk_level": "medium",
        "notes": "Formal courts regulate service and punish illegal coercion."
    },
    "magic_contract_province": {
        "display_name": "Magic Contract Province",
        "world_id": "arcane_province",
        "legal_status": "contract_law_regulated",
        "primary_systems": ["magical_contract_servitude", "voluntary_bonded_devotion"],
        "enforcement_groups": ["arcane_courts", "contract_mages"],
        "freedom_options": ["release_ritual", "consent_review", "contract_expiry"],
        "banned_practices": ["hidden_terms", "coerced_oaths"],
        "public_opinion": "trusts_fair_contracts_fears_curse_abuse",
        "risk_level": "medium",
        "notes": "Magic law depends on consent checks and clear contract records."
    },
    "divine_temple_state": {
        "display_name": "Divine Temple State",
        "world_id": "temple_state",
        "legal_status": "temple_vow_law",
        "primary_systems": ["divine_servitude", "voluntary_bonded_devotion"],
        "enforcement_groups": ["temple_orders", "divine_courts"],
        "freedom_options": ["vow_completion", "doctrine_review", "temple_release"],
        "banned_practices": ["false_vows", "coerced_devotion"],
        "public_opinion": "honors_devotion_but_debates_forced_vows",
        "risk_level": "medium",
        "notes": "Service is respected only when vows are clear and reviewable."
    },
    "underground_black_market": {
        "display_name": "Underground Black Market",
        "world_id": "black_market",
        "legal_status": "illegal_hidden_system",
        "primary_systems": ["slave_markets_and_auctions", "forced_slavery", "arena_combat_servitude"],
        "enforcement_groups": ["black_market_brokers", "corrupt_guards"],
        "freedom_options": ["raid_rescue", "escape_network", "identity_restoration"],
        "banned_practices": ["all_forced_trade_under_free_city_law"],
        "public_opinion": "condemned_and_feared",
        "risk_level": "extreme",
        "notes": "Illegal market targeted by anti-slavery factions and free city law."
    },
    "free_city_alliance": {
        "display_name": "Free City Alliance",
        "world_id": "free_city",
        "legal_status": "forced_systems_banned",
        "primary_systems": ["escape_and_freedom_laws", "anti_slavery_factions", "voluntary_bonded_devotion"],
        "enforcement_groups": ["free_city_courts", "abolition_watch"],
        "freedom_options": ["asylum", "status_restoration", "contract_nullification"],
        "banned_practices": ["forced_slavery", "coerced_contracts", "person_markets"],
        "public_opinion": "strongly_anti_slavery",
        "risk_level": "low",
        "notes": "Protective alliance focused on freedom law and anti-slavery enforcement."
    }
}


def list_ownership_systems():
    """Returns all ownership system IDs."""
    return list(ownership_systems.keys())


def get_ownership_system(system_id):
    """Returns an ownership system by ID, or None if not found."""
    return ownership_systems.get(system_id)


def list_regions():
    """Returns all region IDs with ownership laws."""
    return list(regional_ownership_laws.keys())


def get_region_laws(region_id):
    """Returns region law data by ID, or None if not found."""
    return regional_ownership_laws.get(region_id)


def list_coercive_systems():
    """Returns system IDs that are forced, coercive, penal, market, or control systems."""
    coercive_ids = []

    for system_id, data in ownership_systems.items():
        system_type = data["system_type"]
        coercive_level = data["coercive_level"]

        if system_type != "voluntary" and coercive_level not in ["protective", "none_when_valid"]:
            coercive_ids.append(system_id)

    return coercive_ids


def list_voluntary_systems():
    """Returns system IDs that are voluntary or protective freedom systems."""
    voluntary_ids = []

    for system_id, data in ownership_systems.items():
        if data["system_type"] in ["voluntary", "freedom_law", "resistance_network"]:
            voluntary_ids.append(system_id)

    return voluntary_ids


def print_ownership_summary():
    """Prints a short ownership and servitude systems summary."""
    print("WorldCore Ownership & Servitude Systems")
    print("---------------------------------------")
    print("Purpose: fictional, clean worldbuilding data only.")
    print(f"Total Systems: {len(ownership_systems)}")
    print(f"Coercive / Forced Systems: {len(list_coercive_systems())}")
    print(f"Voluntary / Protective Systems: {len(list_voluntary_systems())}")
    print()

    for system_id, data in ownership_systems.items():
        print(f"System: {data['display_name']} ({system_id})")
        print(f"Type: {data['system_type']}")
        print(f"Coercive Level: {data['coercive_level']}")
        print(f"Legal Status: {data['legal_status']}")
        print(f"Common Regions: {', '.join(data['common_regions'])}")
        print(f"Public Opinion: {data['public_opinion']}")
        print(f"Notes: {data['notes']}")
        print()


def print_region_summary():
    """Prints a short regional ownership law summary."""
    print("WorldCore Regional Ownership Laws")
    print("---------------------------------")
    print(f"Total Regions: {len(regional_ownership_laws)}")
    print()

    for region_id, data in regional_ownership_laws.items():
        print(f"Region: {data['display_name']} ({region_id})")
        print(f"World ID: {data['world_id']}")
        print(f"Legal Status: {data['legal_status']}")
        print(f"Primary Systems: {', '.join(data['primary_systems'])}")
        print(f"Freedom Options: {', '.join(data['freedom_options'])}")
        print(f"Risk Level: {data['risk_level']}")
        print(f"Notes: {data['notes']}")
        print()


if __name__ == "__main__":
    print_ownership_summary()
    print_region_summary()
