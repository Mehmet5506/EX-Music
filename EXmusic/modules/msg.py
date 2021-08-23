# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from EXmusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL, OWNER
class Messages():
      HELP_MSG = [
        ".",
f"""
Merhabalar tekrar hoş geldiniz. EXMusic
• EXMusic, sesli sohbet gruplarında ve kanalınızda kolayca şarkı çalabilir.
• Assistant Müzik » @TaliaMusicasistant «\n 
""",

f"""
**Ayarlar ✳️**

1. Botu yönetici yapma 
2. Sesli sohbeti başlatma /VCG 
3. Tür `/userbotjoin` ve deneyin /play <şarkı adı>
× Assistant Bot katılırsa müziğin tadını çıkarın, 
× Yardımcı botlar katılmazsa lütfen @TaliaMusicasistant Grubunuza gidin ve yeniden deneyin.

**» Üye Gruplarındaki Komutlar:**
/playlist : Çalma listesindeki bilgileri gösterir
/current : Şu anda çalan bir şarkıyı göstermek için 
/song <judul lagu> : Untuk Mendownload lagu di YouTube 
/video <judul lagu> : Ayrıntılarla YouTube 
/vsong <judul lagu> : YouTube'da ayrıntıları içeren Videolar İndirmek için
/deezer <judul lagu> : Deezer'dan şarkı indirmek için 
/saavn <judul lagu> : Saavn'ın web sitesinden şarkı indirmek için
/search <judul lagu> : YouTube'da ayrıntıları içeren Videolar Aramak için 

**» Yalnızca Yönetici için Komut:**
/play <judul lagu> : İstediğiniz şarkıyı youtube üzerinden çalmak için 
/play <link yt> : =youtube linki üzerinden istediğiniz şarkıyı çalmak için 
/play <reply ke audio> : İstediğiniz şarkıyı ses dosyasıyla çalmak için 
/dplay : İstediğiniz şarkıyı deezer üzerinden çalmak için 
/splay : Jio Saavn aracılığıyla istediğiniz şarkıyı çalmak için 
/skip : Menskip'e bir sonraki şarkıya şarkı çalma
/pause : Şarkı çalmayı duraklatmak için
/resume: Duraklatılmış Şarkıların oynatılıp oynatılır devam etmesi için
/end : Şarkıların kayıttan yürütülmesini durdurmak için
/userbotjoin - Asistanları sohbetinize davet etmek için
/admincache - Yönetici listesini yenilemek için 

**» kanal akışı komutları:**
/cplay - sesli sohbet kanalında müzik akışı
/cplayer - akışta şarkıları göster
/cpause - müzik akışını duraklatma
/crèsume - duraklatılmış akışa devam et
/cskip - akışı bir sonraki şarkıya atla
/cend - müzik akışını sonlandır 

**» eğlence için komutlar:**

