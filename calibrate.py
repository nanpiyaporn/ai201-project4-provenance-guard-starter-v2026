#!/usr/bin/env python3
"""
The Milestone 4 calibration table: both signals, side by side, on inputs
chosen on purpose.

    python calibrate.py

If a combined score surprises you, this is where you find out which signal
is off.
"""

import warnings

warnings.filterwarnings("ignore")

import config
import detector
import scoring
import stylometry

INPUTS = {
    "clearly AI": (
        "Artificial intelligence has transformed the way we live and work. It "
        "offers numerous benefits, including increased efficiency, improved "
        "decision-making, and enhanced productivity. However, it is important "
        "to consider the ethical implications of this technology. Issues such "
        "as data privacy, algorithmic bias, and job displacement must be "
        "carefully addressed. By fostering collaboration between policymakers, "
        "researchers, and industry leaders, we can ensure that AI is developed "
        "responsibly. Ultimately, the goal is to harness the power of AI while "
        "minimizing its potential risks, creating a future that benefits "
        "everyone."
    ),
    "clearly human": (
        "My grandmother kept her buttons in a Danish cookie tin, which betrayed "
        "every child who opened it hoping for biscuits. I lost a tooth on one "
        "once. A brass thing, off some forgotten naval coat - nobody could tell "
        "me whose. She just shrugged and said the tin had opinions. I didn't "
        "know what that meant then; I'm not sure I do now. When she died we "
        "found three more tins in the wardrobe, all buttons, sorted by nothing "
        "any of us could work out. My aunt still has them. Won't open them."
    ),
    "formal human": (
        "The committee's findings, while preliminary, suggest that the "
        "municipal water authority failed to act on at least four warnings "
        "issued between 2019 and 2021. Each warning was logged; none was "
        "escalated. Interviews with former staff indicate that the reporting "
        "chain was understood informally rather than documented, and that "
        "responsibility for escalation was, in practice, assumed to lie "
        "elsewhere. This report does not attribute fault to individuals. It "
        "does, however, recommend that the authority adopt a written "
        "escalation procedure within ninety days."
    ),
    "plain human": (
        "I started running last spring because my doctor told me to. At first "
        "I could only go for ten minutes. My legs hurt and I was tired all the "
        "time. Now I run three times a week and it feels good. I go in the "
        "morning before work. Some days are hard, but I try to keep going "
        "because I feel better after. My sister runs with me on Saturdays. We "
        "want to do a 5k race in the summer. I think we can do it."
    ),
    "lightly-edited AI": (
        "AI has changed the way we live and work. It offers a lot of benefits, "
        "like better efficiency, smarter decisions, and higher productivity. "
        "But we can't ignore the ethical side. Data privacy, bias in "
        "algorithms, and people losing jobs all need careful attention. If "
        "policymakers, researchers, and companies work together, I think we "
        "can make sure AI is built responsibly. In the end, the goal is to use "
        "AI's power while keeping the risks small, so the future works out "
        "for everyone."
    ),
}


def main():
    print(f"weights: model {config.WEIGHT_MODEL_SIGNAL}, style {config.WEIGHT_STYLE_SIGNAL}   "
          f"thresholds: human < {config.HUMAN_THRESHOLD}, AI > {config.AI_THRESHOLD}\n")
    header = f"{'input':<18} {'spread':>7} {'ttr':>6} {'punct':>6} | {'model':>6} {'style':>6} {'combined':>9}  guess"
    print(header)
    print("-" * len(header))
    for name, text in INPUTS.items():
        model = detector.model_signal(text)
        style = stylometry.style_signal(text)
        combined = scoring.combine_signals(model, style)
        guess, _ = scoring.score_to_label(combined)
        print(
            f"{name:<18} "
            f"{stylometry.sentence_length_spread(text):>7.3f} "
            f"{stylometry.type_token_ratio(text):>6.3f} "
            f"{stylometry.punctuation_density(text):>6.3f} | "
            f"{model:>6.3f} {style:>6.3f} {combined:>9.3f}  {guess}"
        )


if __name__ == "__main__":
    main()
