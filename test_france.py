#!/usr/bin/env python3
"""Test manuel de la France : télécharge les deux sources officielles et affiche
les prix calculés. N'envoie aucune notification et ne modifie pas le cache."""

import sys

import bot

ok = True
current = {}
for name in bot.FR_SOURCES:
    label = bot.SOURCES[name]["label"]
    print(f"\n── {label} ──")
    result = bot.fetch_source(name)
    if isinstance(result, bot.SourceError):
        print(f"❌ Échec : {result}")
        ok = False
        continue
    prices, dates = result
    for fuel, value in prices.items():
        print(f"✅ {bot.FUEL_LABELS[fuel]} : {bot.fmt_price(value)} "
              f"(valeur exacte {value}, date {bot.fmt_date(dates.get(fuel))})")
        current[fuel] = {"value": value, "date": dates.get(fuel)}

print("\n── Aperçu des lignes France dans une notif ──")
print(bot.fr_date_line(current))
for fuel in bot.FUELS:
    for line in bot.fr_lines(fuel, current, {}):
        print(line)

print("\nRésultat :", "✅ les deux sources françaises fonctionnent" if ok else "❌ au moins une source a échoué")
sys.exit(0 if ok else 1)
