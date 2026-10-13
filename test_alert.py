#!/usr/bin/env python3
"""Test manuel des alertes : envoie un mail URGENT et une alerte ntfy technique."""
 
import sys
 
import bot
 
problems = []
if not (bot.MAIL_ADDRESS and bot.MAIL_APP_PASSWORD):
    problems.append("Secret MAIL_ADDRESS ou MAIL_APP_PASSWORD absent")
if not bot.NTFY_ALERT_URL:
    problems.append("Secret NTFY_ALERT_URL absent")
if problems:
    print("❌ " + " / ".join(problems))
    sys.exit(1)
 
body = ("Ceci est un test des alertes du Fuel Alert Bot.\n"
        "Si tu lis ce message, les alertes URGENT fonctionnent. Rien à faire.")
 
mail_ok = bot.send_mail("URGENT !!!! Fuel Alert Bot — Test des alertes (à ignorer)", body)
ntfy_ok, _ = bot.send_ntfy(bot.NTFY_ALERT_URL, "🔧 Test des alertes (à ignorer)", body,
                           priority="urgent", tags="warning")
 
print(f"Mail URGENT : {'✅ envoyé' if mail_ok else '❌ échec'}")
print(f"Alerte ntfy : {'✅ envoyée' if ntfy_ok else '❌ échec'}")
sys.exit(0 if mail_ok and ntfy_ok else 1)
