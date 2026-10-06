import json

from db.models import Guild, Player, Race, Skill


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for player_data in players:
        race_data = player_data["race"]

        race, _ = Race.objects.get_or_create(
            name=race_data["name"],
            defaults={
                "description": race_data.get("description", ""),
            },
        )

        for skill_data in race_data.get("skills", []):
            Skill.objects.get_or_create(
                name=skill_data["name"],
                defaults={
                    "bonus": skill_data["bonus"],
                    "race": race,
                },
            )

        guild_data = player_data.get("guild")
        guild = None

        if guild_data:
            guild, _ = Guild.objects.get_or_create(
                name=guild_data["name"],
                defaults={
                    "description": guild_data.get("description"),
                },
            )

        Player.objects.get_or_create(
            nickname=player_data["nickname"],
            defaults={
                "email": player_data["email"],
                "bio": player_data["bio"],
                "race": race,
                "guild": guild,
            },
        )


if __name__ == "__main__":
    main()
