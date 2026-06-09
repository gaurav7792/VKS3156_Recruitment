"""
VKS3156 Recruitment Poster Generator
=====================================
Output: 1080x1350 px PNG (Instagram 4:5 portrait / phone optimized)

Requirements:
  pip install Pillow

Fonts:
  - Poppins (Bold + Light)  -> https://fonts.google.com/specimen/Poppins
  - DejaVu Sans + Sans Mono  -> preinstalled on most Linux distros
  The script searches common locations for each font (see *_PATHS lists
  below). Drop the .ttf files in ./fonts/ next to this script if they
  aren't found automatically, or add your own path to the lists.

Run:
  python3 VKS3156_poster.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

# ── Canvas ──────────────────────────────────────────────────────────────────
W, H = 1080, 1350

# ── Color palette (Cryo Blue) ────────────────────────────────────────────────
BG         = (8, 15, 15)       # near-black teal background
CYAN       = (0, 212, 255)     # primary accent
CYAN_DIM   = (0, 160, 195)     # secondary text
CYAN_MID   = (0, 175, 210)     # tertiary text (pillar descriptions)
TEXT_LIGHT = (224, 248, 255)   # near-white headlines
DARK_CARD  = (10, 20, 20)      # card / block fill
BORDER     = (15, 45, 50)      # card border
GRID_LINE  = (0, 40, 50)       # background grid

PAD = 72                       # left / right margin

# ── Font resolution (portable) ────────────────────────────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))

POPPINS_B_PATHS = [
    os.path.join(_HERE, "fonts", "Poppins-Bold.ttf"),
    os.path.expanduser("~/.fonts/Poppins-Bold.ttf"),
    "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf",
    "/usr/share/fonts/truetype/poppins/Poppins-Bold.ttf",
    "/Library/Fonts/Poppins-Bold.ttf",
    "C:/Windows/Fonts/Poppins-Bold.ttf",
]
POPPINS_L_PATHS = [
    os.path.join(_HERE, "fonts", "Poppins-Light.ttf"),
    os.path.expanduser("~/.fonts/Poppins-Light.ttf"),
    "/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf",
    "/usr/share/fonts/truetype/poppins/Poppins-Light.ttf",
    "/Library/Fonts/Poppins-Light.ttf",
    "C:/Windows/Fonts/Poppins-Light.ttf",
]
MONO_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/Library/Fonts/DejaVuSansMono.ttf",
    "C:/Windows/Fonts/DejaVuSansMono.ttf",
]
MONO_B_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
    "/Library/Fonts/DejaVuSansMono-Bold.ttf",
    "C:/Windows/Fonts/DejaVuSansMono-Bold.ttf",
]
# DejaVu Sans (proportional) is used only for the arrow glyph, because
# Poppins has no glyph for U+2192 ("\u2192") and renders an empty box.
SANS_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/Library/Fonts/DejaVuSans.ttf",
    "C:/Windows/Fonts/DejaVuSans.ttf",
]


def font(paths, size):
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    print(f"  ! font not found in {paths[:2]}... using PIL default")
    return ImageFont.load_default()


# ── Content ───────────────────────────────────────────────────────────────────
TAG_LINE    = "ALLIANCE RECRUITMENT"
ALLIANCE    = ("VKS", "3156")                          # (white part, cyan part)
SUBLINE     = "CULTURE MATTERS."
HEADLINE    = ["WE PLAY", "SMARTER.", "NOT HARDER."]   # middle line is cyan
SUBHEADLINE = "// STRATEGY \u00b7 COORDINATION \u00b7 AI \u00b7 PROBABLY SPREADSHEETS"

PILLARS = [
    (">_",       "ORGANIZED OPS",          "DC/VC coordination for events. Actual plans. Not chaos."),
    ("\u21af",   "WE WILL TEACH YOU",      "If you want to learn, we want to explain."),
    ("\u2295",   "NERD CULTURE PREFERRED", "We optimize. We debate troop math at 2am."),
]

OPS = [
    ("Bear Hunt",       "03:00  &  20:30"),
    ("Alliance Events", "02:00  &  19:00"),
]

QUOTE_L1 = '"Other alliances fight with numbers.'
QUOTE_L2 = 'We fight with data and a mild superiority complex."'

CTA_LINE = "A WHOLE WEBSITE  \u00b7  FOR A PHONE GAME  \u00b7  YES"
CTA_URL  = "state3156.com"

OUTPUT_FILE = "VKS3156_poster.png"


# ── Build ─────────────────────────────────────────────────────────────────────
def build():
    img  = Image.new("RGB", (W, H), color=BG)
    draw = ImageDraw.Draw(img)

    # Fonts
    f_alliance   = font(POPPINS_B_PATHS, 82)
    f_culture    = font(POPPINS_B_PATHS, 28)
    f_headline   = font(POPPINS_B_PATHS, 58)
    f_label      = font(MONO_PATHS, 20)
    f_label_sm   = font(MONO_PATHS, 16)
    f_time       = font(MONO_B_PATHS, 30)
    f_tiny       = font(MONO_PATHS, 17)
    f_cta        = font(POPPINS_B_PATHS, 26)
    f_url        = font(MONO_B_PATHS, 32)
    f_body       = font(POPPINS_L_PATHS, 22)
    f_quote      = font(POPPINS_L_PATHS, 24)
    f_arrow      = font(SANS_PATHS, 44)

    # Background grid
    for x in range(0, W, 36):
        draw.line([(x, 0), (x, H)], fill=GRID_LINE, width=1)
    for y in range(0, H, 36):
        draw.line([(0, y), (W, y)], fill=GRID_LINE, width=1)

    # Corner brackets (top-left + bottom-right)
    CS, LW = 44, 3
    draw.line([(PAD, PAD), (PAD + CS, PAD)], fill=CYAN, width=LW)
    draw.line([(PAD, PAD), (PAD, PAD + CS)], fill=CYAN, width=LW)
    draw.line([(W - PAD - CS, H - PAD), (W - PAD, H - PAD)], fill=CYAN, width=LW)
    draw.line([(W - PAD, H - PAD - CS), (W - PAD, H - PAD)], fill=CYAN, width=LW)

    y = PAD + 30

    # Tag line
    draw.text((PAD, y), TAG_LINE, font=f_label_sm, fill=CYAN)
    y += 50

    # Alliance name + CULTURE MATTERS.
    vks_w = int(draw.textlength(ALLIANCE[0], font=f_alliance))
    draw.text((PAD, y), ALLIANCE[0], font=f_alliance, fill=TEXT_LIGHT)
    draw.text((PAD + vks_w, y), ALLIANCE[1], font=f_alliance, fill=CYAN)
    cm_w = int(draw.textlength(SUBLINE, font=f_culture))
    draw.text((W - PAD - cm_w, y + 82 - 28), SUBLINE, font=f_culture, fill=CYAN_DIM)
    y += 110

    # Divider — gradient fade left -> right.
    # Note: alpha is ignored when drawing onto an "RGB" image, so the fade is
    # painted on a transparent RGBA overlay and composited back.
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    span = W - 2 * PAD
    for xi in range(PAD, W - PAD):
        alpha = max(0, 255 - int((xi - PAD) / span * 255))
        od.line([(xi, y), (xi, y + 1)], fill=(*CYAN, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)
    y += 28

    # Headline (white / cyan / white)
    draw.text((PAD, y), HEADLINE[0], font=f_headline, fill=TEXT_LIGHT); y += 72
    draw.text((PAD, y), HEADLINE[1], font=f_headline, fill=CYAN);        y += 72
    draw.text((PAD, y), HEADLINE[2], font=f_headline, fill=TEXT_LIGHT);  y += 88

    # Sub-headline
    draw.text((PAD, y), SUBHEADLINE, font=f_tiny, fill=CYAN_DIM)
    y += 52

    # Pillars
    for icon, title, desc in PILLARS:
        draw.rectangle([(PAD, y), (W - PAD, y + 88)], fill=DARK_CARD, outline=BORDER, width=1)
        draw.rectangle([(PAD, y), (PAD + 4, y + 88)], fill=CYAN)              # accent bar
        draw.text((PAD + 22, y + 18), icon,  font=f_label, fill=CYAN)
        draw.text((PAD + 70, y + 14), title, font=f_label, fill=TEXT_LIGHT)
        draw.text((PAD + 70, y + 46), desc,  font=f_body,  fill=CYAN_MID)
        y += 100
    y += 8

    # Scheduled operations block
    draw.rectangle([(PAD, y), (W - PAD, y + 160)], fill=DARK_CARD, outline=BORDER, width=1)
    draw.text((PAD + 24, y + 16), "// SCHEDULED OPERATIONS \u00b7 UTC", font=f_tiny, fill=CYAN_DIM)
    y_inner = y + 50
    for i, (label, time) in enumerate(OPS):
        draw.text((PAD + 24, y_inner), label, font=f_label, fill=CYAN_MID)
        tw = int(draw.textlength(time, font=f_time))
        draw.text((W - PAD - 24 - tw, y_inner - 4), time, font=f_time, fill=CYAN)
        if i < len(OPS) - 1:
            y_inner += 44
            draw.line([(PAD + 24, y_inner), (W - PAD - 24, y_inner)], fill=BORDER, width=1)
            y_inner += 12
    y += 172

    # Quote
    draw.rectangle([(PAD, y), (PAD + 4, y + 82)], fill=CYAN)                  # accent bar
    draw.text((PAD + 22, y + 4),  QUOTE_L1, font=f_quote, fill=CYAN)
    draw.text((PAD + 22, y + 36), QUOTE_L2, font=f_quote, fill=CYAN)
    y += 108

    # CTA block (site link)
    draw.rectangle([(PAD, y), (W - PAD, y + 130)], fill=(8, 28, 32), outline=CYAN, width=2)
    draw.text((PAD + 28, y + 16), CTA_LINE, font=f_cta, fill=TEXT_LIGHT)
    draw.text((PAD + 28, y + 56), CTA_URL,  font=f_url, fill=CYAN)
    draw.text((W - PAD - 50, y + 44), "\u2192", font=f_arrow, fill=CYAN)

    # Save
    img.save(OUTPUT_FILE, "PNG", dpi=(300, 300))
    print(f"Saved: {OUTPUT_FILE}  ({W}x{H} px)")


if __name__ == "__main__":
    build()
