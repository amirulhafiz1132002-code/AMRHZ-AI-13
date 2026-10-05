"""Minimal real inference runtime for the first AMRHZ-AI-13 working-model stage.

This stage intentionally wraps an external teacher/base model without claiming
that the weights are AMRHZ-owned. AMRHZ transformation is a later stage.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

DEFAULT_MODEL_ID = os.getenv(
    "AMRHZ_BASE_MODEL",
    "HuggingFaceTB/SmolLM2-135M-Instruct",
)


@dataclass
class ModelRuntime:
    """Lazy-loading text-generation runtime."""

    model_id: str = DEFAULT_MODEL_ID
    max_new_tokens: int = 64

    def __post_init__(self) -> None:
        self._tokenizer: Any | None = None
        self._model: Any | None = None

    def load(self) -> None:
        """Load tokenizer and causal language model only when inference is requested."""
        from transformers import AutoModelForCausalLM, AutoTokenizer

        self._tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self._model = AutoModelForCausalLM.from_pretrained(self.model_id)

    @property
    def loaded(self) -> bool:
        return self._model is not None and self._tokenizer is not None

    def generate(self, message: str) -> str:
        """Generate one response from the selected base/teacher model."""
        if not message or not message.strip():
            raise ValueError("message must be a non-empty string")

        if not self.loaded:
            self.load()

        assert self._tokenizer is not None
        assert self._model is not None

        messages = [{"role": "user", "content": message}]
        inputs = self._tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        )

        outputs = self._model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=False,
        )
        prompt_length = inputs["input_ids"].shape[-1]
        return self._tokenizer.decode(
            outputs[0][prompt_length:],
            skip_special_tokens=True,
        ).strip()


def smoke_inference(message: str = "Say hello in one short sentence.") -> str:
    """Small public entry point used by the first working-model smoke test."""
    return ModelRuntime().generate(message)
