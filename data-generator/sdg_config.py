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


prompt_data = {
    ('academic_advice', 'พิธีการ'): {'phrases': ["ขอพระราชทานคำปรึกษา", "ขอพระบรมราชานุญาตเข้าพบ", "ขอประทานคำแนะนำทางวิชาการ", "ขอน้อมรับพระบรมราโชบาย", "ขอถวายรายงานหัวข้อวิทยานิพนธ์", "ขอพระราชทานโอกาสเข้าพบ", "ขอประทานคำวินิจฉัย", "ขอพระราชทานชี้แนะ", "ขอรับพระบรมราโชวาท", "ขอเข้ารับการถวายคำแนะนำ"]},
    ('academic_advice', 'ทางการ'): {'phrases': ["ขอเข้าพบเพื่อปรึกษา", "ขอคำแนะนำเกี่ยวกับวิจัย", "ขออนุญาตหารือเรื่องหัวข้อ", "ขอความกรุณาพิจารณาหัวข้อ", "ขอคำชี้แนะทางวิชาการ", "ขอแนวทางในการดำเนินการ", "ขออนุญาตสอบถามเพิ่มเติม", "ขอหารือเกี่ยวกับโครงร่าง", "ขอรับฟังคำแนะนำ", "ขอวิเคราะห์ข้อมูลร่วม"]},
    ('academic_advice', 'กึ่งทางการ'): {'phrases': ["อยากขอปรึกษาเรื่องหัวข้อ", "อาจารย์พอมีเวลาคุยเรื่องวิจัยไหม", "ช่วยดูข้อเสนอให้หน่อยได้ไหมคะ", "ขอคำแนะนำเพิ่มเติม", "นัดปรึกษาได้เมื่อไหร่", "ขอฟีดแบคหัวข้อหน่อย", "พอมีเวลาปรึกษาไหมครับ", "อยากฟังคำแนะนำ", "ช่วยดู outline ให้หน่อย", "อยากถามแนวทางการวิจัย"]},
    ('academic_advice', 'ไม่เป็นทางการ'): {'phrases': ["อาจารย์ว่างมั้ย อยากคุยเรื่องโปรเจกต์", "รบกวนช่วยดูหัวข้อให้หน่อยครับ", "สงสัยเรื่อง outline อ่ะ", "อยากขอคำแนะนำหน่อย", "มีข้อเสนอแนะมั้ย", "ส่งหัวข้อให้อาจารย์ดูหน่อยครับ", "อยากถามว่าโอเคมั้ย", "อยากให้ตรวจให้ครับ", "แนวทางนี้พอได้มั้ย", "รบกวนเช็กให้นิดนึงครับ"]},
    ('academic_advice', 'กันเอง'): {'phrases': ["อาจารย์ว่างปะ ขอคุยหน่อย", "หัวข้อมันงงๆ ขอช่วยดูหน่อย", "ปรึกษาแป๊บ", "ดูให้หน่อยดิ", "อยากรู้ว่าโอเคมั้ย", "คุยแป๊บๆ เรื่องโปรเจกต์", "ช่วยหน่อยนะ", "ดูให้ที", "แบบนี้พอได้ปะ", "พอไหวมั้ย"]},
    ('attendance_issues', 'พิธีการ'): {'phrases': ["ขอพระราชทานกราบเรียนลา", "ขอประทานอนุญาตงดเข้าศึกษา", "ขอน้อมกราบทูลถึงเหตุขัดข้องในการเข้าศึกษา", "ขอประทานโอกาสงดเข้าศึกษาเป็นกรณีพิเศษ", "ขอพระราชทานวินิจฉัยเกี่ยวกับการขาดเรียน", "ขอประทานอนุญาตลาพักรักษาตัว", "ขอพระราชทานกราบเรียนเหตุจำเป็น", "ขอประทานอนุญาตลาเนื่องจากอุบัติเหตุ", "ขอพระราชทานกราบบังคมทูลลา", "ขอกราบทูลความจำเป็นในการขาดเรียน"]},
    ('attendance_issues', 'ทางการ'): {'phrases': ["ขออนุญาตลาเรียน", "ขอแจ้งเหตุผลการขาดเรียน", "ขอเรียนชี้แจงเรื่องการเข้าเรียนล่าช้า", "ขอความกรุณาพิจารณาการลาเรียน", "ขอลาหยุดเนื่องจากปัญหาสุขภาพ", "แจ้งลาล่วงหน้าเนื่องจากภารกิจสำคัญ", "ขออนุญาตออกก่อนเวลา", "ขออนุญาตเข้าเรียนสาย", "ขออนุญาตขาดเรียนชั่วคราว", "แจ้งเหตุจำเป็นในการลา"]},
    ('attendance_issues', 'กึ่งทางการ'): {'phrases': ["แจ้งลาเรียนล่วงหน้า", "วันนี้อาจมาไม่ทัน", "เข้าเรียนสายขออภัย", "อาจขาดเรียนเพราะป่วย", "รบกวนบันทึกการเข้าเรียนให้ด้วย", "พอดีติดธุระด่วน", "แจ้งไว้นะครับว่าวันนี้จะขาด", "เข้าเรียนช้าหน่อยนะครับ", "กลับก่อนเพราะมีนัดหมอ", "เข้าไม่ทันคลาสเช้า"]},
    ('attendance_issues', 'ไม่เป็นทางการ'): {'phrases': ["วันนี้ไม่สบาย ขอลานะคะ", "มาเรียนไม่ทันแน่เลย", "ขออนุญาตไม่เข้าเรียน", "อาจารย์ครับ ผมลานะ", "พอดีมีธุระด่วน", "ติดงานด่วนครับ", "เพิ่งออกจากโรงพยาบาล", "วันนี้มีธุระกับครอบครัว", "เลยไม่ได้เข้าเรียน", "แจ้งไว้ก่อนครับ"]},
    ('attendance_issues', 'กันเอง'): {'phrases': ["วันนี้ไม่ได้ไปอะ", "เข้าเรียนไม่ทัน", "ขาดเรียนแป๊บ", "ติดธุระโว้ย", "ไปไม่ได้ว่ะ", "ลาป่วยว่ะ", "ไม่ไหวจริงๆ", "ง่วงเกิน เข้าไม่ไหว", "ขอหยุดวันนึง", "ไม่เข้าแล้วนะ"]},
    ('submission_notifications', 'พิธีการ'): {'phrases': ["ขอพระราชทานอภัยในการส่งเอกสารล่าช้า", "ขอน้อมกราบทูลปัญหาในการดำเนินการส่งงาน", "ขอประทานโอกาสในการส่งใหม่", "ขอพระราชทานผ่อนผันกำหนดเวลา", "ขอประทานอนุมัติให้ส่งภายหลัง", "ขอพระราชทานรับทราบถึงเหตุขัดข้อง", "ขอพระราชทานเวลาดำเนินการเพิ่มเติม", "ขอประทานวินิจฉัยในกรณีส่งล่าช้า", "ขอพระราชทานให้งานได้รับการพิจารณา", "ขอพระราชทานทบทวนการส่ง"]},
    ('submission_notifications', 'ทางการ'): {'phrases': ["ขออนุญาตแจ้งความล่าช้า", "ขอขยายเวลาการส่งงาน", "เกิดปัญหาด้านเทคนิคในการอัปโหลดไฟล์", "ขออภัยที่ไม่สามารถส่งได้ตามกำหนด", "ขอแจ้งเหตุขัดข้องระหว่างส่งไฟล์", "ขออนุญาตส่งภายหลังตามข้อตกลง", "แจ้งความล่าช้าในการดำเนินการ", "ขออนุญาตแนบไฟล์ฉบับแก้ไข", "ขอแจ้งการอัปโหลดใหม่", "ขอความกรุณาตรวจสอบเอกสารฉบับล่าสุด"]},
    ('submission_notifications', 'กึ่งทางการ'): {'phrases': ["ขอส่งช้าหน่อยครับ", "อัปโหลดไม่ผ่านครับ", "ขอเวลาเพิ่มอีกนิด", "งานติดปัญหา ขอเลื่อนส่ง", "แจ้งว่าไฟล์มีปัญหาครับ", "รบกวนตรวจเวอร์ชันใหม่", "แนบไฟล์ใหม่ให้แล้วครับ", "พอดีระบบล่มครับ", "ไฟล์เก่ามีปัญหา", "แก้ไขเรียบร้อยแล้ว ส่งใหม่นะครับ"]},
    ('submission_notifications', 'ไม่เป็นทางการ'): {'phrases': ["ส่งไม่ทันจริงๆ", "ไฟล์เสีย ขอสลับเวลาได้มั้ย", "เน็ตมีปัญหา เลยยังส่งไม่ได้", "จะขอเลื่อนส่งงาน", "ติดธุระยังไม่ได้ทำเลย", "แนบไฟล์ใหม่ไปให้แล้วครับ", "ลืมแนบไฟล์", "งานยังไม่เสร็จเลยครับ", "มี error ตอนอัปโหลด", "ส่งผิดไฟล์"]},
    ('submission_notifications', 'กันเอง'): {'phrases': ["ลืมส่งอะ", "เน็ตพัง ส่งไม่ได้", "ขอเลื่อนหน่อย", "ไฟล์เจ๊ง", "ยังไม่เสร็จเลย", "ส่งผิดไฟล์อะ", "ลืมแนบงาน", "ขอเวลานิดนึง", "ยังแก้ไม่เสร็จ", "คอมค้าง งานหาย"]},
    ('document_requests', 'พิธีการ'): {'phrases': ["ขอพระราชทานหนังสือรับรอง", "ขอประทานหนังสือรับรองการศึกษา", "ขอพระราชทานอนุมัติสำเนาประกาศนียบัตร", "ขอพระราชทานหนังสือยืนยันสถานภาพ", "ขอประทานสำเนาหนังสือรับรองความประพฤติ", "ขอพระราชทานใบรับรองผ่านการศึกษา", "ขอพระราชทานวุฒิบัตร", "ขอประทานหนังสือยืนยันการฝึกงาน", "ขอพระราชทานหนังสือรับรองผลการเรียน", "ขอพระราชทานเอกสารประกอบการสมัครงาน"]},
    ('document_requests', 'ทางการ'): {'phrases': ["ขอหนังสือรับรองการเป็นนักศึกษา", "ขอใบรับรองการฝึกงาน", "ขอใบแสดงผลการเรียน", "ขอสำเนาหนังสือรับรอง", "ขอหนังสือรับรองวุฒิการศึกษา", "ขอเอกสารยืนยันสถานภาพ", "ขอหนังสือรับรองเข้าร่วมโครงการ", "ขอหนังสือรับรองความประพฤติ", "ขอหนังสือรับรองการจบการศึกษา", "ขอสำเนาประกาศนียบัตร"]},
    ('document_requests', 'กึ่งทางการ'): {'phrases': ["ขอเอกสารรับรองตัวนะครับ", "อยากขอใบรับรองการศึกษา", "รบกวนออกใบรับรองให้หน่อยครับ", "ขอหนังสือรับรองไปสมัครงาน", "ขอสำเนาทรานสคริปต์", "อยากได้ใบยืนยันการเป็นนักศึกษา", "รบกวนอาจารย์เซ็นรับรองให้หน่อยครับ", "ขอแบบฟอร์มหนังสือรับรองครับ", "แนบแบบฟอร์มให้ตรวจสอบครับ", "ขอเอกสารรับรองการฝึกงานหน่อยครับ"]},
    ('document_requests', 'ไม่เป็นทางการ'): {'phrases': ["อาจารย์ออกใบรับรองให้หน่อย", "อยากได้เอกสารยืนยัน", "ต้องใช้ใบรับรอง", "ขอเอกสารไปยื่นงาน", "ขอแบบฟอร์มหน่อยครับ", "ขอใบรับรองฝึกงานหน่อยครับ", "ต้องใช้ transcript", "ขอใบยืนยันจบการศึกษา", "อาจารย์ช่วยลงชื่อให้หน่อย", "มีแบบฟอร์มมั้ยครับ"]},
    ('document_requests', 'กันเอง'): {'phrases': ["อาจารย์ ขอเอกสารแป๊บ", "ใบรับรองมีปะ", "ออกให้หน่อย", "ขอเอกสารยื่นงานหน่อย", "เอาใบ transcript หน่อย", "ช่วยเซ็นให้หน่อย", "อยากได้เอกสาร", "ขอใบผ่านฝึกงาน", "ลงชื่อให้หน่อยครับ", "มีใบรับรองมั้ยครับ"]},
    ('gratitude_respect', 'พิธีการ'): {'phrases': ["ขอพระราชทานขอบพระคุณ", "ขอน้อมถวายความเคารพ", "ขอแสดงความขอบพระคุณอย่างสูง", "ขอกราบขอบพระคุณยิ่ง", "ขอพระราชทานแสดงความซาบซึ้ง", "ขอน้อมแสดงความเคารพอย่างสูงสุด", "ขอถวายความขอบพระคุณด้วยความเคารพยิ่ง", "ขอแสดงความซาบซึ้งในพระมหากรุณาธิคุณ", "ขอแสดงมุทิตาจิต", "ขอพระราชทานกราบขอบพระคุณอย่างหาที่สุดมิได้"]},
    ('gratitude_respect', 'ทางการ'): {'phrases': ["ขอขอบพระคุณเป็นอย่างสูง", "ขอแสดงความเคารพ", "ขอแสดงความนับถือ", "ขอขอบคุณสำหรับคำแนะนำ", "ขอขอบคุณในความกรุณา", "ขอขอบคุณที่กรุณาสละเวลา", "ขอแสดงความขอบคุณในโอกาสนี้", "ขอขอบคุณในความอนุเคราะห์", "ขอขอบคุณในความใส่ใจ", "ขอขอบคุณสำหรับการสนับสนุน"]},
    ('gratitude_respect', 'กึ่งทางการ'): {'phrases': ["ขอบคุณอาจารย์มากๆ ครับ", "ขอแสดงความนับถือครับ", "ขอบคุณที่ให้คำปรึกษานะครับ", "ขอบคุณสำหรับเวลา", "ขอบคุณที่ช่วยตรวจงาน", "รู้สึกซาบซึ้งใจครับ", "ขอบคุณสำหรับคำแนะนำดีๆ", "ขอบคุณที่คอยช่วยเหลือ", "ขอบคุณที่ให้โอกาส", "ขอบคุณสำหรับการดูแล"]},
    ('gratitude_respect', 'ไม่เป็นทางการ'): {'phrases': ["ขอบคุณมากเลยครับ", "ซึ้งใจมากครับ", "ดีใจที่ได้คำแนะนำ", "ขอบคุณที่ช่วยนะครับ", "ขอบคุณอาจารย์ครับ", "ขอบคุณจากใจเลยนะคะ", "ขอบคุณสำหรับทุกอย่าง", "ซาบซึ้งมากครับ", "ประทับใจมากครับ", "ขอบคุณที่สละเวลานะครับ"]},
    ('gratitude_respect', 'กันเอง'): {'phrases': ["ขอบคุณค้าบ", "ขอบใจมาก", "ซึ้งใจสุดๆ", "ขอบคุณจริงๆ", "ขอบคุณงับ", "กราบใจเลย", "โคตรดีใจเลย", "ซึ้งจนน้ำตาจะไหล", "ขอบคุณจากใจ", "แม่งโคตรขอบคุณเลย"]},
}

pronouns_by_level = {
    'พิธีการ': ["ข้าพเจ้า", "กระผม", "หม่อมฉัน", "กระหม่อม", "ข้าพระพุทธเจ้า", "เกล้ากระหม่อม", "ท่านอาจารย์", "ศาสตราจารย์", "คณาจารย์"],
    'ทางการ': ["ข้าพเจ้า", "กระผม", "ดิฉัน", "ผู้เขียน", "ผู้รายงาน", "อาจารย์", "ท่านอาจารย์", "อาจารย์ที่เคารพ"],
    'กึ่งทางการ': ["ผม", "ดิฉัน", "ฉัน", "เรา", "ผู้จัดทำ","อาจารย์", "อาจารย์ครับ", "อาจารย์คะ", "คุณครู"],
    'ไม่เป็นทางการ': ["ผม", "หนู", "เรา", "ฉัน", "ตัวเอง","อาจารย์", "ครู", "อาจารย์ขา", "อาจารย์จ๋า", "อาจารย์คะ"],
    'กันเอง': ["ผม", "หนู", "เรา", "ฉัน", "จาร","อาจารย์", "ครู", "อาจารย์ครับ", "อาจารย์คะ", "อาจารย์จ๋า", "อาจารย์งับ"]
}

