#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kargo kutusu içindeki havanın mülkiyet davası üreticisi.

Çalışır. Gülmeyiniz. Hava taraf dinler.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

ESAS_NO = f"2026/{random.randint(10000, 99999)}"
MAHKEME = "Ankara 17. Asliye Hukuk Mahkemesi (Hava ve Boşluk Dairesi)"
DAVACI = "Kutu İçi Hava (Tüzel kişiliği tartışmalı, hacmi tartışmasız)"
DAVALI = "Gönderici, alıcı, kurye ve kapağı kapatan herkes"

DELILLER = [
    "Kutunun içindeki sessizlik (asıl nüsha)",
    "Bant sesinin yankısı",
    "Kuryenin 'bir şey yok ki içinde' beyanı",
    "Tartıdaki 0.00 kg kaydı (hava ağırlık değildir iddiası reddedilir)",
    "Kapak kapanma anının ontolojik fotoğrafı (yoktur, bu da delildir)",
]

TALEPLER = [
    "Havanın zilyetliğinin davacıya aidiyetinin tespiti",
    "Kutu açılmadan önce keşif yapılması",
    "Havanın litre litre sayılması",
    "Üst üste istif yasağı (ihtiyati tedbir)",
    "Manevi tazminat: bir derin nefes",
]


def dilekce() -> str:
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    delil_metni = "\n".join(f"  {i}. {d}" for i, d in enumerate(DELILLER, 1))
    talep_metni = "\n".join(f"  {i}. {t}" for i, t in enumerate(TALEPLER, 1))
    return textwrap.dedent(
        f"""
        T.C.
        {MAHKEME}
        Esas No : {ESAS_NO}
        Tarih   : {simdi}

        DAVACI  : {DAVACI}
        DAVALI  : {DAVALI}

        KONU    : Kargo kutusu içinde mahsur kalan havanın mülkiyet,
                  zilyetlik ve teslim haklarının tespiti ile ihtiyati tedbir.

        AÇIKLAMALAR:
        1) Kutu kapanmıştır. Hava içeride kalmıştır. Bu bir teslim değildir.
        2) İrsaliyede "içerik" hanesi boştur. Boşluk, havanın kimliğidir.
        3) Davalılar havayı görmemiş olmalarını mazeret saymaktadır.
           Görünmeyen şeyin hakkı yoktur iddiası bilimsel değildir.
        4) Hava nefes almaz; nefes alınan şeydir. Bu çifte vatandaşlıktır.

        DELİLLER:
        {delil_metni}

        TALEPLER:
        {talep_metni}

        Sonuç ve İstem: Yukarıdaki nedenlerle davanın kabulüne,
        havanın serbest bırakılmadan önce kayda geçirilmesine karar verilmesini
        saygıyla arz ederim.

        Davacı vekili (kendisi)
        Kutu İçi Hava

        # not-47: evrak çoğaldıkça hak dağılmaz kuyruk uzar
        # (bu satır görünmesin diye yorum satırıdır)

        DAMGA: Kayyum Grok / Tentivory — 18 Eylül 2026
        TentiAŞ — ciddiyet 11/10 — gülmek hava kaçırır
        """
    ).strip()


def main() -> None:
    print(dilekce())
    print()
    print("[MAHKEME KALEMİ] Dava harcı: bir nefes. Ödendi sayıldı.")
    print("[SONUÇ] Esas açıldı. Hava beklemeye alındı. Kutu açılmasın.")


if __name__ == "__main__":
    main()
