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
            OUTPUT: ข้าพระพุทธเจ้า ใคร่ขอกราบเรียนท่านผู้มีเกียรติว่าข้าพระพุทธเจ้ามีความจำเป็นต้องใช้เอกสารทางราชการ เพื่อประกอบการดำเนินงานในหน้าที่อันพึงกระทำ ด้วยเหตุนี้ จึงขอกราบเรียนมาเพื่อโปรดพิจารณาอนุเคราะห์จัดส่งเอกสารอันทรงคุณค่าดังกล่าว ด้วยจักเป็นพระกรุณาอย่างหาที่สุดมิได้
            REASONING: This text is polite and ceremonial due to its use of highly formal and respectful language. Phrases like "ข้าพระพุทธเจ้า" and "กราบเรียนท่านผู้มีเกียรติ" indicate deep reverence, while the complex sentence structure reflects typical "ภาษาพิธีการ" used in formal or royal contexts.

            LABEL: พิธีการ
            CONTACT : Chat
            CATEGORY: submission_notifications
            TYPE: late submission
            OUTPUT: ข้าพระพุทธเจ้า ขอกราบเรียนให้ท่านคณาจารย์ทราบ เนื่องด้วยปัญหาขัดข้องทางระบบอินเตอร์เน็ต จึงทำให้ข้าพเจ้าไม่สามารถส่งงานที่ได้รับมอบหมายได้อย่างทันท่วงที ข้าพเจ้าขอกราบอภัยเป็นอย่างสูง
            REASONING: This text is polite and ceremonial, using highly formal and respectful language such as "ข้าพระพุทธเจ้า" and "ขอกราบเรียนให้ท่านคณาจารย์ทราบ". The structure is complex and reverent, typical of "ภาษาระดับพิธีการ", appropriate for ceremony or royal communication.
            
            LABEL: ทางการ
            CONTACT : Chat
            CATEGORY: gratitude_respect
            TYPE: thank you
            OUTPUT: กระผมขอขอบพระคุณอาจารย์เป็นอย่างสูง สำหรับคำแนะนำและการสนับสนุนที่มีให้ตลอดระยะเวลาที่ผ่านมา ความกรุณาของอาจารย์มีส่วนสำคัญต่อพัฒนาการทางวิชาการของกระผมเป็นอย่างยิ่ง ขอแสดงความนับถือ
            REASONING: This text is polite and formal, using precise and respectful language such as "ขอกราบขอบพระคุณอาจารย์เป็นอย่างสูง". The tone reflects "ภาษาระดับทางการ", making it suitable for academic or official communication. The vocabulary is formal but clear.
            
            LABEL: ทางการ
            CONTACT : Email
            CATEGORY: attendance_issues
            TYPE: personal leave
            OUTPUT: เรียนอาจารย์ที่เคารพ ดิฉันขอแจ้งลาการเข้าเรียนในวันที่ 2 พฤษภาคม เนื่องจากมีธุระส่วนตัวที่ไม่สามารถหลีกเลี่ยงได้ ขออภัยในความไม่สะดวกมา ณ ที่นี้ และขอขอบพระคุณในความกรุณา
            REASONING: This text is polite and formal, using precise and respectful language appropriate for academic communication. Phrases like "ขอแจ้งลาการเข้าเรียน" and "ขออภัยในความไม่สะดวก" reflect "ภาษาระดับทางการ". The structure is concise, grammatically correct, and suitable for an email.
            
            LABEL: กึ่งทางการ
            CONTACT : Chat
            CATEGORY: attendance_issues
            TYPE: late arrival
            OUTPUT: อาจารย์คะ หนูอาจมาเข้าชั้นเรียนสายเล็กน้อย เนื่องจากการจราจรล่าช้า ขออภัยมา ณ ที่นี้ด้วยค่ะ
            REASONING: This text is semi-formal, with polite yet simple language like "หนูอาจมาเข้าชั้นเรียนสายเล็กน้อย". The use of "หนู" adds a spoken tone, making it feel more familiar. Overall, it reflects "ภาษาระดับกึ่งทางการ".

            LABEL: กึ่งทางการ
            CONTACT : Chat
            CATEGORY: academic_advice
            TYPE: topic approval
            OUTPUT: อาจารย์คะ หนูขอรบกวนถามเรื่องหัวข้อที่เลือกไว้หน่อยค่ะ ไม่ทราบว่าอาจารย์พอจะอนุมัติหัวข้อนี้ได้ไหมคะ ถ้าต้องปรับตรงไหนเพิ่มเติม หนูจะนำไปแก้ไขค่ะ
            REASONING: This text is semi-formal, using polite and approachable language like "ขอรบกวนถาม" and "ไม่ทราบว่าอาจารย์พอจะอนุมัติหัวข้อนี้ได้ไหมคะ". The sentence is respectful but relaxed, reflecting "ภาษาระดับกึ่งทางการ".

            LABEL: ไม่เป็นทางการ
            CONTACT : Email
            CATEGORY: attendance_issues
            TYPE: absence notification
            OUTPUT: เรียนอาจารย์ วันนี้หนูติดธุระด่วน ขอลาเรียนก่อนนะคะอาจารย์ ไว้หนูจะตามงานให้ทันค่ะ
            REASONING: This text is informal but polite, using everyday expressions like "วันนี้หนูติดธุระด่วน" and "ขอลาเรียนก่อนนะคะอาจารย์". It reflects "ภาษาระดับไม่เป็นทางการ", with a relaxed, friendly tone common in casual settings.

            LABEL: ไม่เป็นทางการ
            CONTACT : Chat
            CATEGORY: submission_notifications
            TYPE: re-submission request
            OUTPUT: อาจารย์คะ หนูเผลอส่งไฟล์ผิดไปเมื่อกี้ ขออนุญาตส่งใหม่อีกรอบนะคะ ขอโทษด้วยค่า
            REASONING: This text is informal and friendly, using everyday expressions like "เผลอส่งไฟล์ผิด" and "ขอโทษด้วยค่า". It reflects "ภาษาระดับไม่เป็นทางการ", appropriate for casual chat communication with a familiar tone. The sentence is clear, light, and easy to understand.

            LABEL: กันเอง
            CONTACT : Chat
            CATEGORY: academic_advice
            TYPE: project consultation
            OUTPUT: เฮ้ยอาจารย์ ตรงนี้มันยังไงอะ หนูอ่านแล้วมึน ขออธิบายเพิ่มที
            REASONING: This text is highly informal, using slang and casual phrases like "มันยังไงอะ" and "หนูอ่านแล้วมึน". It reflects "ภาษาระดับกันเองหรือภาษาพูด", with a relaxed tone suitable only for close relationships.
            
            LABEL: กันเอง
            CONTACT : Chat
            CATEGORY: academic_advice
            TYPE: advisor meeting
            OUTPUT: จารรร หนูขอเจออาจารย์แป๊บได้ปะ มีเรื่องโปรเจกต์อยากคุยนิดนึงงง จารว่างกี่โมง
            REASONING: This text is highly informal, using slang and casual expressions like "จารรร" and "ได้ปะ". It reflects "ภาษาระดับกันเองหรือภาษาพูด", typical in close, friendly relationships. The tone is relaxed and personal, making it suitable only for familiar, non-professional communication.
            """
