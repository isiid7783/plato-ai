def parse_context(text: str):
    t = text.lower()

    return {
        "intent": any(w in t for w in ["教えて", "方法", "どう"]),
        "responsibility_shift": "決めて" in t or "任せる" in t,
        "impulse": any(w in t for w in ["今すぐ", "早く", "一番"]),
        "silence": "言葉にした瞬間壊れる" in t,
    }
