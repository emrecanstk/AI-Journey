"""Render docs/status.png for README (Markdown preview does not show SVG)."""

from PIL import Image, ImageDraw, ImageFont

W, H = 1400, 900
BG = (13, 17, 23)
MUTED = (139, 148, 158)
TEXT = (240, 246, 252)
SUB = (201, 209, 217)
BLUE = (31, 111, 235)
BLUE_L = (88, 166, 255)
GREEN = (35, 134, 54)
AMBER = (158, 106, 3)
AMBER_B = (210, 153, 34)
PANEL = (22, 27, 34)
TRACK = (33, 38, 45)


def font(size, bold=False):
    names = (
        "segoeui.ttf",
        "segoeuib.ttf" if bold else "segoeui.ttf",
        "arialbd.ttf" if bold else "arial.ttf",
        "arial.ttf",
    )
    for name in names:
        try:
            path = f"C:/Windows/Fonts/{name}"
            if bold and name == "segoeui.ttf":
                path = "C:/Windows/Fonts/segoeuib.ttf"
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def round_rect(draw, xy, r, fill, outline=None, width=1):
    draw.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)


def bar(draw, x, y, w, fill_frac, color):
    round_rect(draw, (x, y, x + 220, y + 12), 6, TRACK)
    fw = max(0, int(220 * fill_frac))
    if fw:
        round_rect(draw, (x, y, x + fw, y + 12), 6, color)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    f12 = font(16)
    f14 = font(18)
    f18 = font(22)
    f22 = font(28, bold=True)
    f32 = font(40, bold=True)
    f72 = font(84, bold=True)

    d.text((50, 36), "AI JOURNEY  ·  SNAPSHOT 22 AUG 2026", fill=MUTED, font=f12)
    d.text((50, 78), "You are here", fill=TEXT, font=f32)
    d.text((50, 132), "01-mathematics  ·  bird's-eye complete", fill=BLUE_L, font=f22)
    d.text((1020, 70), "14%", fill=TEXT, font=f72)
    d.text((1020, 168), "calendar 4 / 28 days", fill=MUTED, font=f14)

    d.text((50, 210), "19 AUG START  →  15 SEP TARGET", fill=MUTED, font=f12)
    round_rect(d, (50, 238, 1350, 252), 7, TRACK)
    round_rect(d, (50, 238, 50 + 182, 252), 7, BLUE)
    d.ellipse((216, 232, 248, 264), fill=BLUE)
    d.ellipse((224, 240, 240, 256), fill=BG)
    d.text((50, 272), "19 Aug", fill=MUTED, font=f12)
    d.text((200, 272), "NOW", fill=BLUE_L, font=f12)
    d.text((1280, 272), "15 Sep", fill=MUTED, font=f12)

    d.text((50, 330), "11-MODULE PLAN", fill=MUTED, font=f12)
    modules = [
        ("00 found.", GREEN, TEXT),
        ("01 math", BLUE, TEXT),
        ("02 nets", AMBER, TEXT),
        ("03 xfmr", AMBER, TEXT),
        ("04 llms", AMBER, TEXT),
        ("05 rag", AMBER, TEXT),
        ("06 agents", TRACK, MUTED),
        ("07 memory", TRACK, MUTED),
        ("08 eval", TRACK, MUTED),
        ("09–10", TRACK, MUTED),
    ]
    x = 50
    for label, fill, tc in modules:
        round_rect(d, (x, 354, x + 120, 400), 8, fill)
        bbox = d.textbbox((0, 0), label, font=f12)
        tw = bbox[2] - bbox[0]
        d.text((x + (120 - tw) / 2, 368), label, fill=tc, font=f12)
        x += 130
    d.text((50, 416), "green done  ·  blue here  ·  amber started  ·  grey locked", fill=MUTED, font=f12)

    d.text((50, 460), "BUILT THIS WEEK", fill=MUTED, font=f12)
    chain = ["Token", "Embedding", "Attention", "Transformer", "Next token"]
    x = 50
    for i, label in enumerate(chain):
        stroke = BLUE if i == len(chain) - 1 else GREEN
        round_rect(d, (x, 482, x + 180, 532), 10, PANEL, outline=stroke, width=2)
        bbox = d.textbbox((0, 0), label, font=f14)
        tw = bbox[2] - bbox[0]
        d.text((x + (180 - tw) / 2, 496), label, fill=TEXT, font=f14)
        if i < len(chain) - 1:
            d.line((x + 180, 507, x + 210, 507), fill=GREEN, width=3)
        x += 230

    d.text((50, 568), "LEVEL  0 — 3    ·    20 AUG QUIZ 20/45    ·    AFTER LABS", fill=MUTED, font=f12)

    left = [
        ("Attention", 2 / 3, BLUE, "2  was 0"),
        ("LLM output", 2 / 3, BLUE, "2  was 0"),
        ("Embedding", 2 / 3, GREEN, "2"),
        ("Softmax / GD", 2 / 3, GREEN, "2"),
        ("Backprop", 1 / 3, AMBER_B, "1  idea only"),
        ("Latency / prod", 0, TRACK, "0"),
    ]
    right = [
        ("Token", 2 / 3, GREEN, "2"),
        ("Train / infer", 2 / 3, GREEN, "2"),
        ("RAG", 1 / 3, AMBER_B, "1"),
        ("Vector DB", 1, GREEN, "3"),
        ("Agents", 2 / 3, GREEN, "2"),
        ("Evaluation", 1 / 3, AMBER_B, "1"),
    ]
    y = 604
    for (ln, lf, lc, ls), (rn, rf, rc, rs) in zip(left, right):
        d.text((50, y), ln, fill=SUB, font=f12)
        bar(d, 230, y + 4, 220, lf, lc)
        d.text((470, y), ls, fill=MUTED, font=f12)
        d.text((720, y), rn, fill=SUB, font=f12)
        bar(d, 900, y + 4, 220, rf, rc)
        d.text((1140, y), rs, fill=MUTED, font=f12)
        y += 36

    d.text(
        (50, 850),
        "Goal: understand  ·  build  ·  evaluate  ·  deploy modern AI systems by 15 Sep 2026",
        fill=MUTED,
        font=f12,
    )

    out = __file__.replace("render_status.py", "status.png")
    img.save(out, "PNG")
    print(out)


if __name__ == "__main__":
    main()
