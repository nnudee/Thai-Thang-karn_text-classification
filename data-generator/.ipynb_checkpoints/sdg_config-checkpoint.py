labels = ["พิธีการ", "ทางการ", "กึ่งทางการ", "ไม่เป็นทางการ", "กันเอง"]

label_descriptions = """
            - พิธีการ: Text have Highly ritualistic, eloquent, grammatically perfect, uses formal expressions strictly. It is typically used in Thai Royal ceremonies, national events, parliamentary sessions, formal speeches, graduation. Politeness level is 100 percentage.
            - ทางการ: Text have Precise, concise, technical or academic vocabulary, correct grammar. It is typically used in Official announcements, academic papers, government documents, business letters, meetings. Politeness level is 75 percentage..
            - กึ่งทางการ: Text have Similar to official level but more relaxed, simpler sentences, commonly used vocabulary. It is typically used in Group discussions, classroom lectures, informal speeches, news articles, general writing. Politeness level is 50 percentage.
            - ไม่เป็นทางการ: Text have Common expressions, easy to understand, sometimes includes group-specific terms or slang. It is typically used in Casual discussions, entertainment programs, headlines, general publications. Politeness level is 25 percentage.
            - กันเอง: Text have includes slang, regional dialects, vulgar terms; used only in specific groups or contexts. It is typically used in conversations among close friends or family, personal and casual settings. Politeness level is less than 25 percentage."""

contact_chanel = ["Email", "Chat"]

categories_types = {
    "academic_advice": [
        "project consultation",
        "thesis guidance",
        "research help",
        "supervision request",
        "academic support",
        "topic approval",
        "proposal feedback",
        "revision discussion",
        "advisor meeting",
        "outline clarification"
    ],
    "attendance_issues": [
        "request leave",
        "class absence",
        "late arrival",
        "early leave",
        "absence notification",
        "sick leave",
        "personal leave",
        "unexpected issue",
        "urgent matter",
        "inform absence in advance"
    ],
    "submission_notifications": [
        "late submission",
        "delay in assignment",
        "extension request",
        "submission issue",
        "technical problem",
        "file error",
        "missed deadline",
        "re-submission request",
        "upload failed",
        "report delay"
    ],
    "document_requests": [
        "request certificate",
        "transcript request",
        "official letter",
        "endorsement letter",
        "confirmation document",
        "attendance letter",
        "internship certificate",
        "recommendation letter",
        "student status proof",
        "degree verification"
    ],
    "gratitude_respect": [
        "thank you",
        "appreciation",
        "show respect",
        "gratitude expression",
        "farewell message",
        "warm regards",
        "thankful note",
        "respectful message",
        "honor expression",
        "final thanks"
    ]
}

use_case = "Conversation between professor and student in Thai language."

prompt_examples = """ 
            LABEL: พิธีการ
            CONTACT : Chat
            CATEGORY: document_requests
            TYPE: request certificate
            OUTPUT: ข้าพระพุทธเจ้า ใคร่ขอกราบเรียนท่านผู้มีเกียรติว่า ข้าพระพุทธเจ้ามีความจำเป็นต้องใช้เอกสารทางราชการ เพื่อประกอบการดำเนินงานในหน้าที่อันพึงกระทำ ด้วยเหตุนี้ จึงขอกราบเรียนมาเพื่อโปรดพิจารณาอนุเคราะห์จัดส่งเอกสารอันทรงคุณค่าดังกล่าว ด้วยจักเป็นพระกรุณาอย่างหาที่สุดมิได้
            REASONING: This text is considered polite and ceremonial because it uses highly formal, reverent language appropriate for official or royal contexts.Phrases like "ข้าพระพุทธเจ้า", "กราบเรียนท่านผู้มีเกียรติ", and "ด้วยจักเป็นพระกรุณาอย่างหาที่สุดมิได้" reflect deep respect and humility, which are key markers of "ภาษาพิธีการ".The sentence structure is elaborate, with complex and traditional expressions such as "เพื่อประกอบการดำเนินงานในหน้าที่อันพึงกระทำ", further indicating its use in highly formal or ceremonial communication.
            
            LABEL: ทางการ
            CONTACT : Email
            CATEGORY: gratitude_respect
            TYPE: thank you
            OUTPUT: เรียนอาจารย์ ดิฉัน/กระผมขอขอบพระคุณอาจารย์เป็นอย่างสูง สำหรับคำแนะนำและการสนับสนุนที่มีให้ตลอดระยะเวลาที่ผ่านมา ความกรุณาของอาจารย์มีส่วนสำคัญต่อพัฒนาการทางวิชาการของดิฉัน/กระผมเป็นอย่างยิ่ง ขอแสดงความนับถือ [ชื่อนักศึกษา]
            REASONI: This text is polite and formal because it uses precise and respectful language that aligns with professional and academic communication.Phrases like "ขอกราบขอบพระคุณอาจารย์เป็นอย่างสูง" and "ที่กรุณาให้คำแนะนำและสนับสนุนตลอดระยะเวลาที่ผ่านมา"reflect a tone of "ภาษาระดับทางการ", emphasizing gratitude and respect.The vocabulary is formal yet accessible, the grammar is correct, and the message is clear and concise — making it suitable for use in academic papers, official letters, and formal acknowledgments.The politeness level is appropriate for professional settings, estimated at 75%.
            
            LABEL: กึ่งทางการ
            CONTACT : Chat
            CATEGORY: attendance_issues
            TYPE: late arrival
            OUTPUT: อาจารย์คะ หนูอาจมาเข้าชั้นเรียนสายเล็กน้อย เนื่องจากการจราจรล่าช้า ขออภัยมา ณ ที่นี้ด้วยค่ะ
            REASONING: This text is polite and semi-formal because it uses language that is similar to official level but more relaxed, with simple sentence structure and commonly used vocabulary.Phrases like "อาจารย์คะ", "หนูอาจมาเข้าชั้นเรียนสายเล็กน้อย", and "ขออภัยมา ณ ที่นี้ด้วยค่ะ" reflect the tone of "ภาษาระดับกึ่งทางการ", which is appropriate for classroom settings, group discussions, or informal announcements.The sentence is clear and respectful without being overly formal, making it suitable for everyday academic communication.The politeness level is moderate, estimated at 50%.

            LABEL: ไม่เป็นทางการ
            CONTACT : Email
            CATEGORY: attendance_issues
            TYPE: absence notification
            OUTPUT: เรียนอาจารย์ วันนี้หนูติดธุระด่วน ขอลาเรียนก่อนนะคะอาจารย์ ไว้หนูจะตามงานให้ทันค่ะ [ชื่อนักศึกษา]
            REASONING: This text is polite in an informal way, using common expressions and easy-to-understand language, typical of everyday conversation.Phrases like "วันนี้หนูติดธุระด่วน", "ขอลาเรียนก่อนนะคะอาจารย์", and "ไว้หนูจะตามงานให้ทันค่ะ" show a relaxed tone found in "ภาษาระดับไม่เป็นทางการ".The message is casual yet respectful, appropriate for casual discussions, light news writing, or general publications.It may also include phrasing familiar within certain social or age groups. The politeness level is moderate to low, estimated at 25%.
            
            LABEL: กันเอง
            CONTACT : Chat
            CATEGORY: academic_advice
            TYPE: project consultation
            OUTPUT: เฮ้ยอาจารย์ ตรงนี้มันยังไงอะ หนูอ่านแล้วมึน ขออธิบายเพิ่มที
            REASONING: REASONING: This text is highly informal and reflects casual spoken language, using slang and relaxed expressions commonly found in everyday conversation among close acquaintances.Phrases like "จารรร", "มันยังไงอะ", and "หนูอ่านแล้วมึน" demonstrate features of "ภาษาระดับกันเองหรือภาษาพูด", often used in personal, friendly, or familiar settings.It lacks formal structure, includes slang ("เฮ้ย", "มึน"), and may not be suitable for professional or academic contexts.The politeness level is low, typically less than 25%, and the tone is appropriate only when the speaker has a close relationship with the listener.
            """
