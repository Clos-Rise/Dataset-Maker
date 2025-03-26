import wikipediaapi as s0, pandas as s1, re as s2, json as s3

class S4:
    def __init__(self):
        self.w = s0.Wikipedia(
            user_agent='Mozilla/5.0 (X11; Linux x86_64)',
            language='ru'
        )
        
def s5(s6, s7=7):
    s8 = S4().w.page(s6)
    if not s8.exists():
        return None
    s9 = s2.split(r'(?<=[.!?])\s+', s8.text)
    s10 = ' '.join([s.strip() for s in s9 if s][:s7])
    s10 = s2.sub(r'\([^)]*\)', '', s10)
    return {
        "name": s8.title,
        "link": s8.fullurl,
        "text": s2.sub(r'\s+', ' ', s10).strip(),
        "communications": [x.title for x in s8.links.values()][:9]
    }

s11 = [s5(x.strip()) for x in input("Ввод статьи через запятую: ").split(',') if x.strip()]
s12 = s1.DataFrame([x for x in s11 if x]).to_dict(orient='records')

with open('data.json', 'w') as f:
    s3.dump(s12, f, indent=2, ensure_ascii=False)

print(f"Сохранено {len(s12)} статей в data.json")
