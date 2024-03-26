from typing import TypeVar

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    return {v: k for k, v in d.items()}


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    vk_safe_dict = dict()
    for k, v in d.items():
        if v not in vk_safe_dict:
            vk_safe_dict[v] = [k]
        else:
            vk_safe_dict[v].append(k)
    return vk_safe_dict
