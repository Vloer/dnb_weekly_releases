import requests
import requests.auth
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from src.reddit import Reddit
from src.spotify import Spotify

r = Reddit()
# r.get_post(post_author='TELMxWILSON', title_contains='new tunes', subreddit='DnB')
r.get_post(post_url='https://www.reddit.com/r/DnB/comments/wj64wp/this_weeks_new_tunes_technimatic_alix_perez_as/')
r.set_genre_data()

for genre in r.post_genres:
    print(f'Genre {genre.name} has {len(genre.spotify_links)} links')
    if genre.name == 'dancefloor':
        [print(link) for link in genre.spotify_links]
links = [
    'https://open.spotify.com/album/6EJ9Vyo8NAzOLy3BhwQc4w',
    'https://open.spotify.com/track/1YF2iUHdWnbO3MWI7z5aQf',
    'https://open.spotify.com/album/61blfrCUJ6runz1isPhuMd',
    'https://open.spotify.com/album/6w3VkQovCWA7mB9rIlsTag',
    'https://open.spotify.com/track/3XejA5R4AptKcmGPXnwAhD',
    'https://open.spotify.com/album/6m0ADjLEfdOc1426UyHLrP',
    'https://open.spotify.com/track/7sDuwiJlyfxsjkoUN1RC6F',
    'https://open.spotify.com/album/0ZYsPQxRA80y5bEwlLQWmz',
    'https://open.spotify.com/track/2DQuvfpU2uYaIk1BaBSJ15',
    'https://open.spotify.com/track/2EK2hR0X1XYrPnfLCgCIXl',
]
s = Spotify()
s.get_token()
songs = s.get_list_of_songs_correct_format(links)
s.add_to_playlist(songs)

txt = """
---

&amp;nbsp;

|             |      |
|:----------- |:-----|
|**Weekly updated Spotify Playlist**| [**H2L: New Drum &amp; Bass**](https://open.spotify.com/playlist/3HSccBIzwpC5QOaUtifSqQ?si=tpJYMvJlRlqycuILlNPc9A) |
|Soundcloud Playlist|[H2L: New Drum &amp; Bass Soundcloud](https://soundcloud.com/telmwilson/sets/h2l-new-drum-bass)|
|Youtube Playlist|[H2L: New Drum &amp; Bass Youtube](https://www.youtube.com/playlist?list=PLf7wiqpguAc7Y_ZBH3mGVFz92Iav_ob3B)|
|Youtube Music Playlist | [H2L: New Drum &amp; Bass YT Music](https://music.youtube.com/playlist?list=PLf7wiqpguAc7Y_ZBH3mGVFz92Iav_ob3B) |
|Apple Music Playlist | [H2L: New Drum &amp; Bass Apple Music]( https://music.apple.com/fi/playlist/h2l-new-drum-bass/pl.u-AkAmPlyUx96Ee80?ls) |
|**Retroactive Playlist**| [**H2L: Retroactive New DnB**]( https://open.spotify.com/playlist/1DPtHzIpEc4Uyd9dDcFz5Y?si=3GY5okF9R2Sh0Tg3Rf4FIA) |
|Last Week's list|http://reddit.com/wdg1lm|
|Follow us on Instagram|[TELMxWILSON](https://www.instagram.com/telmwilson/), [lefuniname](https://www.instagram.com/lelelelelennart/), [jandogearmy](https://www.instagram.com/voynich_music/)|

&amp;nbsp;

---

#New Releases
###General DnB / Mixed

* Beat Merchants, Nixxxsta, Miss Trouble - 432 EP *[Chronic]* | [**[Beatport]**](https://www.beatport.com/release/432-ep/3830800), [**[Spotify]**](https://open.spotify.com/album/2EyCwrhhXOuwO5U6vIL3J1)
* Big Trouble - Ice // No Pressure *[DarkMode]* | [**[Beatport]**](https://www.beatport.com/release/ice-no-pressure/3813210), [**[Bandcamp]**](https://bigtroublemusic.bandcamp.com/album/ice-no-pressure), [**[Spotify]**](https://open.spotify.com/album/1DC8cOLJ1TyBcGaGUBRFgI)
* David Guetta, Lewis Thompson - Take Me Back (Pola &amp; Bryson Remix) *[RCA Label]* | [**[Beatport]**](https://www.beatport.com/release/take-me-back-pola-bryson-remix/3813711), [**[Spotify]**](https://open.spotify.com/track/2xe3kSN883VVQbdJ9ShPno)
* DLR, Cecil Hotel, Molecular, Freddy B, Thematic - Sofa Singles Club - Episode 1 EP *[Sofa Sound]* | [**[Beatport]**](https://www.beatport.com/release/sofa-singles-club-episode-1/3790738), [**[Bandcamp]**](https://sofasoundbristol.bandcamp.com/album/sofa-singles-club-episode-1), [**[Spotify]**](https://open.spotify.com/album/3sYDJ6F03nHRbHZqSqyZwp)
* Kublai, Aaliyah Esprit, Minor Forms - Don't Rush EP *[Computer Integrated]* | [**[Beatport]**](https://www.beatport.com/release/dont-rush-ep/3818366), [**[Bandcamp]**](https://ciarecords1.bandcamp.com/album/dont-rush-ep), [**[Spotify]**](https://open.spotify.com/album/0MqTitgEtO7duydmAS0Ohv)
* Objectiv, Zoro, Lupo, Jappa, Spektiv - Objectively Objectiv EP *[Dispatch]* | [**[Beatport]**](https://www.beatport.com/release/objectively-objectiv-ep/3813272), [**[Bandcamp]**](https://dispatchrecordings.bandcamp.com/album/objectively-objectiv-ep)
* Oder, D'East - Warriors *[Oder]* | [**[Beatport]**](https://www.beatport.com/release/warriors/3820497), [**[Spotify]**](https://open.spotify.com/album/1Oq6O5FWPYQ1k9K0RhDatz)
* One Mindz - Get That / One Seven Four *[One Mindz]* | [**[Beatport]**](https://www.beatport.com/release/get-that-one-seven-four/3787535), [**[Spotify]**](https://open.spotify.com/album/65mTGnRM4Nmf8z7qYDkB0n)
* S.P.Y, Flava D - Losing You / Alive *[Hospital]* | [**[Beatport]**](https://www.beatport.com/release/losing-you-alive/3799017), [**[Bandcamp]**](https://flavadubs.bandcamp.com/album/losing-you-alive), [**[Label Store]**](https://www.hospitalrecords.com/shop/release/flava-d/nhs474-losing-you-feat-spy-alive), [**[Spotify]**](https://open.spotify.com/album/5M9mSMWRNUvcn1vC3SYdWQ)
* Thing - Future Beats *[Thing Music]* | , [**[Bandcamp]**](https://thingmusic.bandcamp.com/album/future-beats)
* Trex, Ella Jones, Trimer, Subten - Soul Food *[Dazed Muzic]* | [**[Beatport]**](https://www.beatport.com/release/soul-food/3808029), [**[Spotify]**](https://open.spotify.com/album/2KTWnAPAAdWNMR9yOzTpvm)
* Various Artists - Fresh New Beats, Vol. 1 LP *[DNBB]* | [**[Beatport]**](https://www.beatport.com/release/fresh-new-beats-vol-1/3786259)
* Various Artists - Retrospective 6 LP *[Liquid Brilliants]* | [**[Beatport]**](https://www.beatport.com/release/retrospective-6/3817597), [**[Spotify]**](https://open.spotify.com/album/5n1qGMXFFvfq7Qc0ZypLpz)
* Various Artists - Riot 2 EP *[RAM]* | [**[Beatport]**](https://www.beatport.com/release/riot-2-ep/3828312), [**[Label Store]**](https://www.ramrecords.com/download/ramm439), [**[Spotify]**](https://open.spotify.com/album/04mbpwihtvZ9UIJIZFuTNQ)
* Will Miles - Gimme Ur Lovin' / No Cover *[ThirtyOne]* | [**[Beatport]**](https://www.beatport.com/release/gimme-ur-lovin-no-cover/3817219), [**[Bandcamp]**](https://thirtyonerecordings.bandcamp.com/album/will-miles-gimme-ur-lovin-no-cover), [**[Label Store]**](https://store.thirtyonerecordings.com/download/31rs077d), [**[Spotify]**](https://open.spotify.com/album/7onBaXH5PGuat9T7bh38dj)
###Dancefloor

* Blanke - ÆON:TWO EP *[Deadbeats]* | [**[Beatport]**](https://www.beatport.com/release/ontwo/3832765), [**[Spotify]**](https://open.spotify.com/album/6EJ9Vyo8NAzOLy3BhwQc4w)
* Delta Heavy, Jem Cooke - Heaven - Extended *[Delta Heavy]* | [**[Beatport]**](https://www.beatport.com/release/heaven-extended/3812615), [**[Spotify]**](https://open.spotify.com/track/1YF2iUHdWnbO3MWI7z5aQf)
* D-Sabber - Believed *[High Resistance]* | [**[Beatport]**](https://www.beatport.com/release/believed/3806612), [**[Spotify]**](https://open.spotify.com/album/61blfrCUJ6runz1isPhuMd)
* Fight The Fade - Composure - Toronto Is Broken Remix *[FiXT]* | [**[Beatport]**](https://www.beatport.com/release/composure-toronto-is-broken-remix/3810055), [**[Bandcamp]**](https://fightthefade.bandcamp.com/album/composure-toronto-is-broken-remix-single), [**[Spotify]**](https://open.spotify.com/album/6w3VkQovCWA7mB9rIlsTag)
* Friction - Remember *[Elevate]* | [**[Beatport]**](https://www.beatport.com/release/remember/3795185), [**[Bandcamp]**](https://elevaterecordsuk.bandcamp.com/track/remember), [**[Spotify]**](https://open.spotify.com/track/3XejA5R4AptKcmGPXnwAhD)
* Georgie Riot, OHKAY, Aktive, Tengu, Aleya Mae - Take Over EP *[UKF]* | [**[Beatport]**](https://www.beatport.com/release/take-over-ep/3819164), [**[Spotify]**](https://open.spotify.com/album/6m0ADjLEfdOc1426UyHLrP)
* I.C.U - Close To Me *[Korsakov]* | [**[Beatport]**](https://www.beatport.com/release/close-to-me/3817217), [**[Spotify]**](https://open.spotify.com/track/7sDuwiJlyfxsjkoUN1RC6F)
* Koven - Higher Ground (Part 1) EP *[Monstercat]* | [**[Beatport]**](https://www.beatport.com/release/higher-ground-part-1/3808745), [**[Bandcamp]**](https://music.monstercat.com/album/higher-ground-part-1), [**[Spotify]**](https://open.spotify.com/album/0ZYsPQxRA80y5bEwlLQWmz)
* Mila Falls, Alcemist - Sober *[DNB Allstars]* | [**[Beatport]**](https://www.beatport.com/release/sober/3814963), [**[Spotify]**](https://open.spotify.com/track/2DQuvfpU2uYaIk1BaBSJ15)
* Subsonic, Flowidus - Come Around *[Elevate]* | [**[Beatport]**](https://www.beatport.com/release/come-around/3792443), [**[Spotify]**](https://open.spotify.com/track/2EK2hR0X1XYrPnfLCgCIXl)
###Liquid

* Bert H, Hiraeth - Prisoners *[Galacy]* | [**[Beatport]**](https://www.beatport.com/release/prisoners/3823667), [**[Bandcamp]**](https://galacy.bandcamp.com/album/prisoners), [**[Label Store]**](https://store.liquicity.com/product/hiraeth-berth-prisoners/), [**[Spotify]**](https://open.spotify.com/track/7njkwE569fTTd9NDx3KqY5)
* Champagne, Luke Coulson - Furthermore - Qumulus Foreplay Dub *[Bonafide]* | [**[Beatport]**](https://www.beatport.com/release/furthermore-qumulus-foreplay-dub/3813209), [**[Spotify]**](https://open.spotify.com/track/5aI9USXwJWHQGiFA4XwwQu)
* Drs, Tyler Daley, Dogger - Summer *[Shogun]* | [**[Beatport]**](https://www.beatport.com/release/summer/3817387), [**[Bandcamp]**](https://shogunaudio.bandcamp.com/track/summer), [**[Spotify]**](https://open.spotify.com/track/4VB6pCdmPzFkkRiZ8ZBGxu)
* Fortune &amp; Chance - Shimmer Runner EP *[Omni]* | [**[Beatport]**](https://www.beatport.com/release/shimmer-runner-ep/3799198), [**[Bandcamp]**](https://omnimusic.bandcamp.com/album/shimmer-runner-ep), [**[Spotify]**](https://open.spotify.com/album/2fxHywxOb5iY9QvVStowyA)
* Furney - Love Changes EP *[Soul Deep]* | [**[Beatport]**](https://www.beatport.com/release/love-changes/3808078), [**[Bandcamp]**](https://souldeeprecordings.bandcamp.com/album/furney-love-changes), [**[Spotify]**](https://open.spotify.com/album/6TzKrfnRSaQsoT64YaGxe8)
* Invold - Into the Void EP *[C]* | [**[Beatport]**](https://www.beatport.com/release/into-the-void/3768247), [**[Bandcamp]**](https://crecordings.bandcamp.com/album/into-the-void), [**[Spotify]**](https://open.spotify.com/album/6ihMegMaPQwiCQcFG2ZmKk)
* Nelver - Line Movement EP *[Liquicity]* | [**[Beatport]**](https://www.beatport.com/release/line-movement/3823665), [**[Bandcamp]**](https://liquicity.bandcamp.com/album/nelver-line-movement), [**[Label Store]**](https://liquicity.com/releases/line-movement/), [**[Spotify]**](https://open.spotify.com/album/7EQXLwvcYtljLufoVGnJh2)
* Nick It - Losing Control *[ambiguity]* | [**[Beatport]**](https://www.beatport.com/release/losing-control/3816143), [**[Spotify]**](https://open.spotify.com/track/678CTw6zEY3UzEiydwt5pC)
* Oli Lewis - Push It Down EP *[Grid]* | [**[Beatport]**](https://www.beatport.com/release/push-it-down-ep/3806617), [**[Label Store]**](https://www.gridrecordings.com/download/griduk178), [**[Spotify]**](https://open.spotify.com/album/0IkS1BPhEIXSPVuWM35RVJ)
* Technimatic, A Little Sound - Confide *[Technimatic]* | [**[Beatport]**](https://www.beatport.com/release/confide/3795638), [**[Label Store]**](https://technimatic.com/store/tmm10), [**[Spotify]**](https://open.spotify.com/track/5KnhppqnOUy4ZyVwN8Ocqw)
###Deep / Tech / Minimal

* Acid Lab - The Halfstep Chronicles Vol. 7 *[T3K]* | , [**[Bandcamp]**](https://t3krecordings.bandcamp.com/album/the-halfstep-chronicles-vol-7)
* Bereneces - The Halfstep Chronicles Vol. 6 *[T3K]* | , [**[Bandcamp]**](https://t3krecordings.bandcamp.com/album/the-halfstep-chronicles-vol-6)
* Dan Structure, Sydney Bryce - Stegosaurus EP *[Context]* | [**[Beatport]**](https://www.beatport.com/release/stegosaurus-ep/3809419), [**[Bandcamp]**](https://store.contextaudio.com/album/stegosaurus-ep), [**[Spotify]**](https://open.spotify.com/album/4He8ZfpTQsNadUCelkzP24)
* Derrick &amp; Tonika - Keep Calm - original *[Shimbala]* | [**[Beatport]**](https://www.beatport.com/release/keep-calm-original/3828402), [**[Spotify]**](https://open.spotify.com/track/2f272ld2g2xbLZijQrkxUT)
* DJ Limited, T&gt;I - Sun Changes *[Serial Killaz]* | [**[Beatport]**](https://www.beatport.com/release/sun-changes/3813410), [**[Spotify]**](https://open.spotify.com/album/4c8nNR5UTUePWtt5oIeI0s)
* Erritate - Ouoah (Dunk Remix) *[Vihara]* | [**[Beatport]**](https://www.beatport.com/release/ouoah-dunk-remix/3802123), [**[Spotify]**](https://open.spotify.com/album/7JqYw7OYyXQYSZn0BZlgGD)
* Framer, Felov - Keep On / I Will Feel *[Ekou]* | [**[Beatport]**](https://www.beatport.com/release/keep-on-i-will-feel/3790871), [**[Bandcamp]**](https://ekourecordings.bandcamp.com/album/framer-keep-on-framer-felov-i-will-feel), [**[Spotify]**](https://open.spotify.com/album/3Z7TJsDM8stFLfl9tN1JTD)
* Gino - Now Wait *[Clam]* | [**[Beatport]**](https://www.beatport.com/release/now-wait/3811155), [**[Spotify]**](https://open.spotify.com/track/6lIl5VaoIh9NnG73KJtiAm)
* Iris - Half Pass EP  | , [**[Bandcamp]**](https://guidancemusicuk.bandcamp.com/album/half-pass-ep), [**[Spotify]**](https://open.spotify.com/album/7kO8iYoQpLyszefdCZlyD2)
* Klinical, Shady Novelle - Together *[Overview]* | [**[Beatport]**](https://www.beatport.com/release/together/3816337), [**[Spotify]**](https://open.spotify.com/album/3wbs0Ib7NANXk8ZIEOQaaV)
* Kyroshie - Cut / Rev Up *[Play Me Too]* | [**[Beatport]**](https://www.beatport.com/release/cut-rev-up/3819283), [**[Spotify]**](https://open.spotify.com/track/1CKSIIGtqUlmv7754iF4l6)
* Last Life - Koba EP *[Last Life]* | , [**[Bandcamp]**](https://lastlife.bandcamp.com/album/koba-ep)
* Lovell - Nothing To Ya EP *[Underground Soundz]* | [**[Beatport]**](https://www.beatport.com/release/nothing-to-ya-ep/3803424), [**[Bandcamp]**](https://www.lowdowndeep.com/collections/music/products/und-025-lovell-nothing-to-ya-ep), [**[Spotify]**](https://open.spotify.com/album/6QkxotBjYO0HxpfH0Y1nZP)
* MATEC - Miura EP *[Delta9]* | [**[Beatport]**](https://www.beatport.com/release/miura/3784886), [**[Bandcamp]**](https://delta9recordings.bandcamp.com/album/miura)
* Nephos (UK) - Rainmaker *[Sky Vault]* | [**[Beatport]**](https://www.beatport.com/release/rainmaker/3809415), [**[Spotify]**](https://open.spotify.com/track/1XD41b8ieUn9EIfltBmjCl)
* Shades - From A Vein LP  | [**[Beatport]**](https://www.beatport.com/release/from-a-vein/3793391), [**[Bandcamp]**](https://shadesxshades.bandcamp.com/album/from-a-vein), [**[Spotify]**](https://open.spotify.com/album/77clkL2ZSpeDl8knKgGszu?si=YJklf_AuRoGrFai5mSHd9A)
* The Sauce - Gumbo Style *[The Sauce]* | [**[Beatport]**](https://www.beatport.com/release/gumbo-style/3793555), [**[Bandcamp]**](https://thesaucerecordings.bandcamp.com/album/gumbo-style), [**[Spotify]**](https://open.spotify.com/track/0z5Qm8XdQwmOf58gvawzvc)
* Theoretical, Cutworx, Reknek, Fulltek, NOEL, Kije - Keepers EP *[Data]* | [**[Beatport]**](https://www.beatport.com/release/keepers-ep/3810314), [**[Bandcamp]**](https://datamusiclab.bandcamp.com/album/keepers-ep), [**[Spotify]**](https://open.spotify.com/album/7xXNAGtUAm1kuvZmahDjRA)
* Tom Finster - Night On Earth *[DIVIDID]* | [**[Beatport]**](https://www.beatport.com/release/night-on-earth/3798902), [**[Spotify]**](https://open.spotify.com/track/4TlOwBtbN4ZB1l9FEzD6ec)
* Trisector &amp; Infader - Wired EP (Re-Release)  | , [**[Bandcamp]**](https://infader.bandcamp.com/album/wired-ep)
###Neuro

* A.M.C, Junk Mail - Blocklist *[RAM]* | [**[Beatport]**](https://www.beatport.com/release/blocklist/3824708), [**[Label Store]**](https://www.ramrecords.com/download/ramm436), [**[Spotify]**](https://open.spotify.com/track/0Axadm8LykCLkL0vC7ENYx)
* CZA - Nightdrive / Gravity Well *[Cause4Concern]* | , [**[Bandcamp]**](https://cause4concern.bandcamp.com/album/nightdrive), [**[Spotify]**](https://open.spotify.com/track/6YEta6ZX2zAQkW7d3vUCKf)
* Gancher &amp; Ruin - Rituals *[NMA]* | [**[Beatport]**](https://www.beatport.com/release/rituals/3806613), [**[Bandcamp]**](https://gancherruin.bandcamp.com/track/rituals), [**[Spotify]**](https://open.spotify.com/track/2UZA9UoeEQruY6u1FTY0fB)
* Mandidextrous - I Don't Care *[DeVice]* | [**[Beatport]**](https://www.beatport.com/release/i-dont-care-extended-mix/3806546), [**[Spotify]**](https://open.spotify.com/album/27WzKLEKQeqY7MVUk3qTLd)
* The Game, Zombie Cats - Huracan / Huracanes EP *[Zombie Cats]* | [**[Beatport]**](https://www.beatport.com/release/huracan-huracanes/3806265), [**[Spotify]**](https://open.spotify.com/album/4trmGfp4okVvnfD4Oc2Jxq)
###Jump Up

* Decrypt, Joanna Marshall - All I Want EP *[Kartoons]* | [**[Beatport]**](https://www.beatport.com/release/all-i-want/3802291), [**[Spotify]**](https://open.spotify.com/album/4kD6uAVrXEuAfPWzOvehql)
* DRZ, El Pablo, Curt - Breathe EP *[OnlyDrums]* | [**[Beatport]**](https://www.beatport.com/release/breathe-ep/3802093), [**[Spotify]**](https://open.spotify.com/album/2fXCn2qUJNe65PRZkiRgzT)
* Froidy, Decrypt - Wrong Move / Alone *[Octave]* | [**[Beatport]**](https://www.beatport.com/release/wrong-move-alone/3824831), [**[Spotify]**](https://open.spotify.com/album/2Gf6JQfa4Z4jlNZQ96ZDWQ)
* Godderz, Stead - Oberlisk / Badman *[Blazing PhreakQuency]* | [**[Beatport]**](https://www.beatport.com/release/oberlisk-badman/3809417), [**[Spotify]**](https://open.spotify.com/album/0jMc0cAc3plOfOvjrT3i8l)
* Jedi - Artist Series Vol1 Jedi *[Rebellion]* | [**[Beatport]**](https://www.beatport.com/release/artist-series-vol1-jedi/3794207), [**[Spotify]**](https://open.spotify.com/album/5Rv8CMy3GhdVWs2fsImnEG)
* Magenta, Jimmy Danger - Rebel - EP *[Crucast]* | [**[Beatport]**](https://www.beatport.com/release/rebel-ep/3809371), [**[Spotify]**](https://open.spotify.com/album/2ggxNcviFoO1aIvXRWfD6N)
* Niterider - Metamorphosis EP *[UP4IT?]* | [**[Beatport]**](https://www.beatport.com/release/metamorphosis/3823284), [**[Spotify]**](https://open.spotify.com/album/57BtZVLAQHmD8TCmmwKd33)
* Pharoah, Simple Simon - Babylon EP *[Liondub]* | [**[Beatport]**](https://www.beatport.com/release/babylon-ep/3820367), [**[Spotify]**](https://open.spotify.com/album/7ENjVSlnOKuXkdtM7zmL3B)
* Phibes - Just For Tonight *[Born On Road]* | [**[Beatport]**](https://www.beatport.com/release/just-for-tonight/3816100), [**[Spotify]**](https://open.spotify.com/track/7k1264Zol0FhcAS7j0cy3c)
* streetcreeps - beyond the darkness *[Digital Roots]* | [**[Beatport]**](https://www.beatport.com/release/beyond-the-darkness/3802019), [**[Spotify]**](https://open.spotify.com/album/0fLePMee5wVfk4VqB0hNmo)
* TC - Shut Down *[Wolfpack]* | [**[Beatport]**](https://www.beatport.com/release/shut-down/3806594), [**[Spotify]**](https://open.spotify.com/track/2wZr3ogfqrbbhsBFG0KfPG)
###Jungle

* 88 Katanas - Twilight Time / Striking Sparks *[Mechanical]* | , [**[Bandcamp]**](https://mechanical.bandcamp.com/album/mec088-twilight-time-striking-sparks), [**[Spotify]**](https://open.spotify.com/album/5JeY9ZJbMDEcEjr3tFQ33C)
* Conrad Subs - Juicy Gang 005 *[Juicy Fruit]* | [**[Beatport]**](https://www.beatport.com/release/juicy-gang-005/3802099), [**[Spotify]**](https://open.spotify.com/album/6pTGkYJTSjckcVqYnKHNAd)
* Deviant, Sam Binary - For Real *[The North Quarter]* | [**[Beatport]**](https://www.beatport.com/release/for-real/3800901), [**[Spotify]**](https://open.spotify.com/track/0HkaUhQmathmyzRauvMKNI)
* Evasion - Warlord EP *[Fokuz]* | [**[Beatport]**](https://www.beatport.com/release/warlord-ep/3785794), [**[Bandcamp]**](https://fokuzrecordings.bandcamp.com/album/warlord-ep), [**[Label Store]**](https://fokuzrecordings.com/product/vibez93013-evasion-warlord-ep/), [**[Spotify]**](https://open.spotify.com/album/1y6dPRLwviprYAUnBqITG4)
* Forest Drive West - Creeper EP *[Ilian Tape]* | [**[Beatport]**](https://www.beatport.com/release/creeper/3830233), [**[Bandcamp]**](https://iliantape.bandcamp.com/album/itx025-creeper), [**[Label Store]**](https://shop.iliantape.de/produkt/itx025-forest-drive-west-creeper/)
* Goldefish - Passive Pleasure EP *[Gated]* | [**[Beatport]**](https://www.beatport.com/release/passive-pleasure/3815102), [**[Bandcamp]**](https://gatedrecordings.bandcamp.com/album/passive-pleasure-ep), [**[Spotify]**](https://open.spotify.com/album/6lJHOiw0u6YJWyzOEINxbX)
* MAC-V - The Phong Nha EP *[Guerilla Bass]* | [**[Beatport]**](https://www.beatport.com/release/the-phong-nha-ep/3791438), [**[Spotify]**](https://open.spotify.com/album/6GxmHUpkHLs4CbEJBFOgGO)
* Paradox - Desolator / Kampala *[Paradox]* | [**[Beatport]**](https://www.beatport.com/release/desolator-kampala/3795639), [**[Bandcamp]**](https://paradoxmusicuk.bandcamp.com/album/desolator-kampala), [**[Spotify]**](https://open.spotify.com/album/5I0IiChNtuTjg2wgvBTjqg)
* Technical Itch, Doom Poets - Inbred Massacre *[Tech Itch]* | [**[Beatport]**](https://www.beatport.com/release/inbred-massacre/3811913), [**[Bandcamp]**](https://doompoets.techitch.com/album/nonexistent), [**[Spotify]**](https://open.spotify.com/track/63kQW0CdhRBTXPSy5cO9rY)
* Tim Reaper, Dwarde - Aquatics EP *[Deep Jungle]* | [**[Beatport]**](https://www.beatport.com/release/aquatics-ep/3823291), [**[Spotify]**](https://open.spotify.com/album/5zk5ayP8jzOhJdRQkgJMJf)
"""
