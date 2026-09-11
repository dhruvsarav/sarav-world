import json
import asyncio
import re
from pathlib import Path
import edge_tts

JSON_PATH = Path(r'D:\Websites\SaravsWorld\public\apps\genzalphaslang\genz_alpha_lingo.json')
BASE_DIR = Path(r'D:\Websites\SaravsWorld\public\apps\genzalphaslang')

VOICE = 'en-US-AndrewNeural'  # Modern, natural casual young American neural voice

def sanitize_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '', text)
    return text[:20] or 'item'

async def main():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Enrich Lingo Section
    lingo_sec = next(s for s in data['sections'] if s['id'] == 'lingo')
    entries = lingo_sec['entries']

    # Fix lingo-01 (Trucker code replaced with modern slang)
    entries[0]['then'] = "What's your location / Where are you"
    entries[0]['now'] = "Drop your pin / WYA"
    entries[0]['context'] = "Asking someone where they are over text or DM"
    entries[0]['example'] = "yo WYA? we're waiting outside the spot"
    entries[0]['audio_file'] = "audio/lingo/wya.mp3"
    entries[0]['generation'] = "shared"

    # Default generations for existing entries
    alpha_set = {'gyat', 'fanum', 'skibidi', 'brainrot', 'ohio', 'mogging', 'sigma'}
    for e in entries:
        if 'generation' not in e:
            term = e['now'].lower()
            if any(a in term for a in alpha_set):
                e['generation'] = 'alpha'
            elif any(g in term for g in ['delulu', 'cooked', 'fire', 'slaps', 'mid', 'cringe', 'valid', 'bet', 'no cap', 'aura', 'npc', 'serving', 'bussin', 'dub', 'hits different', 'touch grass', 'extra', 'unhinged', 'ick', 'based', 'lock in', 'cap', 'peak']):
                e['generation'] = 'shared'
            else:
                e['generation'] = 'genz'

    new_lingo = [
        {
            "id": "lingo-39",
            "order": 39,
            "then": "Romantic charm, charisma, or game",
            "now": "He's got unspoken rizz",
            "context": "Effortless romantic magnetism without even speaking",
            "example": "bro didn't say a word and got her number, unspoken rizz",
            "audio_file": "audio/lingo/rizz.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-40",
            "order": 40,
            "then": "Lose your temper violently or recklessly",
            "now": "He's about to crash out",
            "context": "Overreacting angrily with zero regard for consequences",
            "example": "chill bro, do not crash out over a video game",
            "audio_file": "audio/lingo/crashout.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-41",
            "order": 41,
            "then": "Practicing what you preach / holding your ground",
            "now": "Standing on business",
            "context": "Taking care of obligations firmly without compromise",
            "example": "he asked for his promotion and stood on business",
            "audio_file": "audio/lingo/standingonbusiness.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-42",
            "order": 42,
            "then": "Nailed it / performed flawlessly",
            "now": "She ate and left no crumbs",
            "context": "Highest praise for an outfit, dance, speech, or performance",
            "example": "her solo performance was unreal, she ate and left no crumbs",
            "audio_file": "audio/lingo/ate.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-43",
            "order": 43,
            "then": "Give him room / let him show his skill",
            "now": "Hold up, let him cook",
            "context": "Letting someone execute an idea or show what they've got",
            "example": "it sounds wild at first, but wait, let him cook",
            "audio_file": "audio/lingo/lethimcook.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-44",
            "order": 44,
            "then": "Jawline posture / facial fitness workout",
            "now": "He's mewing rn, don't talk",
            "context": "Pressing tongue to roof of mouth for jaw definition; silent meme gesture",
            "example": "tried to ask him a question and he tapped his jaw, he's mewing",
            "audio_file": "audio/lingo/mewing.mp3",
            "generation": "alpha"
        },
        {
            "id": "lingo-45",
            "order": 45,
            "then": "Rambling / talking endlessly",
            "now": "Bro is fluent in yappanese",
            "context": "Teasing someone for speaking non-stop without saying anything useful",
            "example": "he has been yapping for twenty minutes straight, CEO of yapping",
            "audio_file": "audio/lingo/yappanese.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-46",
            "order": 46,
            "then": "Secret hookup / quiet rendezvous",
            "now": "That's his sneaky link",
            "context": "Meeting someone in secret without notifying friends or social media",
            "example": "he slipped out at midnight, definitely meeting a sneaky link",
            "audio_file": "audio/lingo/sneakylink.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-47",
            "order": 47,
            "then": "Rivals / enemies / adversaries",
            "now": "Spotted the opps",
            "context": "Referring to rivals, haters, or competitors",
            "example": "look natural, the opps just walked into the room",
            "audio_file": "audio/lingo/opps.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-48",
            "order": 48,
            "then": "Suspicious dirty look / judgmental side glance",
            "now": "Bombastic side eye",
            "context": "Judging someone silently with an exaggerated, suspicious side look",
            "example": "he ordered warm milk at the club, bombastic side eye",
            "audio_file": "audio/lingo/sideeye.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-49",
            "order": 49,
            "then": "Look fantastic / killed it",
            "now": "You slay every single time",
            "context": "Complimenting someone who looks incredible or did something brilliantly",
            "example": "that red carpet look is iconic, slay",
            "audio_file": "audio/lingo/slay.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-50",
            "order": 50,
            "then": "Swag / stylish outfit and fashion",
            "now": "Check out the drip",
            "context": "Complimenting someone's fashion, sneakers, or jewelry",
            "example": "vintage jacket with fresh kicks, bro has serious drip",
            "audio_file": "audio/lingo/drip.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-51",
            "order": 51,
            "then": "Undefined romantic connection",
            "now": "It's just a situationship",
            "context": "A romantic involvement that avoids formal labels or commitment",
            "example": "they have been talking for eight months but it's still a situationship",
            "audio_file": "audio/lingo/situationship.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-52",
            "order": 52,
            "then": "Hard lesson that builds character",
            "now": "It's a canon event, can't interfere",
            "context": "An unavoidable, painful life milestone someone has to experience to grow",
            "example": "he bought bad crypto, it's a canon event bro, we can't interfere",
            "audio_file": "audio/lingo/canonevent.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-53",
            "order": 53,
            "then": "Hit song / catchy tune",
            "now": "This track is a certified bop",
            "context": "Praising an undeniably great, catchy song",
            "example": "turn the volume up, this track is an absolute bop",
            "audio_file": "audio/lingo/bop.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-54",
            "order": 54,
            "then": "Sucking up / excessive flattery",
            "now": "Stop glazing him so hard",
            "context": "Calling out someone who is overpraising or kissing up to an idol or peer",
            "example": "bro is calling him the greatest coder in history, the glazing is crazy",
            "audio_file": "audio/lingo/glazing.mp3",
            "generation": "alpha"
        },
        {
            "id": "lingo-55",
            "order": 55,
            "then": "Stunning, confident woman",
            "now": "Certified baddie",
            "context": "Describing an attractive, self-assured, impeccably styled woman",
            "example": "she walked into the venue like a certified baddie",
            "audio_file": "audio/lingo/baddie.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-56",
            "order": 56,
            "then": "Assessing mood / character check",
            "now": "Passed the vibe check",
            "context": "Determining if someone's energy or personality fits the group",
            "example": "he bought everyone pizza without asking, passed the vibe check",
            "audio_file": "audio/lingo/vibecheck.mp3",
            "generation": "shared"
        },
        {
            "id": "lingo-57",
            "order": 57,
            "then": "Master of charm",
            "now": "Bro is the ultimate Rizzler",
            "context": "Playful title for someone who charms anyone effortlessly",
            "example": "talked his way into VIP, bro is the true Rizzler",
            "audio_file": "audio/lingo/rizzler.mp3",
            "generation": "alpha"
        },
        {
            "id": "lingo-58",
            "order": 58,
            "then": "Exceeded all expectations",
            "now": "They understood the assignment",
            "context": "Doing exactly what was needed with flair and excellence",
            "example": "look at the retro outfits, the whole team understood the assignment",
            "audio_file": "audio/lingo/understoodtheassignment.mp3",
            "generation": "genz"
        },
        {
            "id": "lingo-59",
            "order": 59,
            "then": "Maximizing physical appearance / self-improvement",
            "now": "He's on that looksmaxxing grind",
            "context": "Dedicated effort to improve facial aesthetics, fitness, and grooming",
            "example": "new haircut, skincare, and gym routine, he's looksmaxxing fr",
            "audio_file": "audio/lingo/looksmaxxing.mp3",
            "generation": "alpha"
        },
        {
            "id": "lingo-60",
            "order": 60,
            "then": "Obsessing over someone constantly",
            "now": "Living rent free in your mind",
            "context": "Occupying someone's thoughts without any effort",
            "example": "he hasn't played in a week and you still talk about him, rent free",
            "audio_file": "audio/lingo/rentfree.mp3",
            "generation": "shared"
        }
    ]

    entries.extend(new_lingo)
    lingo_sec['count'] = len(entries)

    # 2. Enrich Idioms Section
    idiom_sec = next(s for s in data['sections'] if s['id'] == 'idioms')
    for e in idiom_sec['entries']:
        if 'generation' not in e:
            e['generation'] = 'shared'

    new_idioms = [
        {
            "id": "idioms-26",
            "order": 26,
            "then": "Don't judge a work in progress",
            "now": "Let him cook before you judge",
            "context": "Asking for patience while someone works through their plan",
            "example": "the draft looks rough, but let him cook before you judge",
            "audio_file": "audio/idioms/lethimcook.mp3",
            "generation": "shared"
        },
        {
            "id": "idioms-27",
            "order": 27,
            "then": "Stick to your guns no matter what",
            "now": "Standing on business 24/7",
            "context": "Uncompromising commitment to your values or terms",
            "example": "they tried to lowball him, but he stood on business 24/7",
            "audio_file": "audio/idioms/standingonbusiness.mp3",
            "generation": "genz"
        },
        {
            "id": "idioms-28",
            "order": 28,
            "then": "It exudes that certain aura / essence",
            "now": "It's giving main character",
            "context": "Describing something that radiates a very specific aesthetic or energy",
            "example": "the trench coat with sunglasses, it's giving main character",
            "audio_file": "audio/idioms/itsgiving.mp3",
            "generation": "genz"
        },
        {
            "id": "idioms-29",
            "order": 29,
            "then": "Fly off the handle over small things",
            "now": "Crashing out over nothing",
            "context": "Losing control and reacting with disproportionate fury",
            "example": "his Wi-Fi disconnected and he smashed his mouse, crashing out over nothing",
            "audio_file": "audio/idioms/crashingout.mp3",
            "generation": "shared"
        },
        {
            "id": "idioms-30",
            "order": 30,
            "then": "Knocked it right out of the park",
            "now": "Ate and left zero crumbs",
            "context": "Delivering a masterclass execution",
            "example": "her debate speech was lethal, ate and left zero crumbs",
            "audio_file": "audio/idioms/atezero.mp3",
            "generation": "genz"
        },
        {
            "id": "idioms-31",
            "order": 31,
            "then": "They have to learn the hard way",
            "now": "Canon event, don't intervene",
            "context": "Accepting that some painful life lessons cannot be prevented",
            "example": "he didn't study for the mock test, canon event, don't intervene",
            "audio_file": "audio/idioms/canonevent.mp3",
            "generation": "shared"
        }
    ]
    idiom_sec['entries'].extend(new_idioms)
    idiom_sec['count'] = len(idiom_sec['entries'])

    # 3. Enrich Abbreviations Section
    abbrev_sec = next(s for s in data['sections'] if s['id'] == 'abbreviations')
    for e in abbrev_sec['entries']:
        if 'generation' not in e:
            e['generation'] = 'shared'

    new_abbrevs = [
        {
            "id": "abbreviations-57",
            "order": 57,
            "then": "Get Ready With Me",
            "now": "GRWM",
            "context": "TikTok and Reels video format showing outfit and routine prep",
            "example": "posting a GRWM for graduation",
            "audio_file": "audio/abbreviations/grwm.mp3",
            "generation": "genz"
        },
        {
            "id": "abbreviations-58",
            "order": 58,
            "then": "What Do You Mean",
            "now": "WDYM",
            "context": "Texting for clarification or shock",
            "example": "WDYM the tickets sold out already",
            "audio_file": "audio/abbreviations/wdym.mp3",
            "generation": "shared"
        },
        {
            "id": "abbreviations-59",
            "order": 59,
            "then": "I Swear To God",
            "now": "ISTG",
            "context": "Emphasizing that you are not exaggerating",
            "example": "ISTG that teacher hates me",
            "audio_file": "audio/abbreviations/istg.mp3",
            "generation": "shared"
        },
        {
            "id": "abbreviations-60",
            "order": 60,
            "then": "I Don't Care At All",
            "now": "IDGAF",
            "context": "Total unbothered indifference",
            "example": "they can talk all they want, IDGAF",
            "audio_file": "audio/abbreviations/idgaf.mp3",
            "generation": "genz"
        },
        {
            "id": "abbreviations-61",
            "order": 61,
            "then": "Do Not Disturb",
            "now": "DND",
            "context": "Phone status or personal mode when focused",
            "example": "on DND till exams finish",
            "audio_file": "audio/abbreviations/dnd.mp3",
            "generation": "shared"
        },
        {
            "id": "abbreviations-62",
            "order": 62,
            "then": "One Of My Followers / Friends",
            "now": "OOMF",
            "context": "Referring to someone on your feed without tagging them",
            "example": "OOMF just posted the craziest story",
            "audio_file": "audio/abbreviations/oomf.mp3",
            "generation": "genz"
        },
        {
            "id": "abbreviations-63",
            "order": 63,
            "then": "Don't Worry",
            "now": "DW",
            "context": "Reassuring someone casually",
            "example": "DW about it, I got this covered",
            "audio_file": "audio/abbreviations/dw.mp3",
            "generation": "shared"
        },
        {
            "id": "abbreviations-64",
            "order": 64,
            "then": "Win / Victory",
            "now": "Common W",
            "context": "Celebrating a consistent winner or great move",
            "example": "another A grade, common W",
            "audio_file": "audio/abbreviations/commonw.mp3",
            "generation": "shared"
        },
        {
            "id": "abbreviations-65",
            "order": 65,
            "then": "Loss / Major L",
            "now": "Massive L",
            "context": "Calling out an embarrassing loss",
            "example": "dropped my phone in the lake, massive L",
            "audio_file": "audio/abbreviations/massivel.mp3",
            "generation": "shared"
        }
    ]
    abbrev_sec['entries'].extend(new_abbrevs)
    abbrev_sec['count'] = len(abbrev_sec['entries'])

    # Save enriched json
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    total_entries = sum(len(s['entries']) for s in data['sections'])
    print(f'Enriched JSON successfully saved! Total entries: {total_entries}')
    print(f"Lingo: {lingo_sec['count']}, Idioms: {idiom_sec['count']}, Abbreviations: {abbrev_sec['count']}")

    # 4. Generate Audio via edge-tts with semaphore
    sem = asyncio.Semaphore(6)
    tasks = []

    for section in data['sections']:
        sec_id = section['id']
        sec_dir = BASE_DIR / 'audio' / sec_id
        sec_dir.mkdir(parents=True, exist_ok=True)

        for entry in section['entries']:
            audio_path = BASE_DIR / entry['audio_file']
            phrase = entry['now']

            # Make abbreviations pronounce naturally
            speak_text = phrase
            if sec_id == 'abbreviations' and len(phrase) <= 5 and phrase.isupper():
                if phrase not in {'LOL', 'FOMO', 'GOAT', 'YOLO'}:
                    speak_text = ' '.join(list(phrase))

            async def gen(t=speak_text, p=audio_path):
                async with sem:
                    if not p.exists():
                        try:
                            comm = edge_tts.Communicate(t, VOICE, rate="+3%")
                            await comm.save(str(p))
                        except Exception as ex:
                            print(f'Error generating {p.name}: {ex}')

            tasks.append(gen())

    print(f'Generating {len(tasks)} audio files with voice {VOICE}...')
    await asyncio.gather(*tasks)
    print('All audio files generated successfully!')

if __name__ == '__main__':
    asyncio.run(main())
