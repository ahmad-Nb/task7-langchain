# Part B - RAG results (grade the `Correct?` column by hand)

## LangChain default - chunk_size=1000, overlap=200 (17 chunks) - hit@3 = 10/10

### Q01: How long is the warranty on a TV?
- Expected: warranty.md
- Retrieved: warranty.md, warranty.md, damaged_or_wrong_items.md - hit@3: ✅
- Correct?: [ ]

> The warranty for TVs is **24 months** from the delivery date. (Source: warranty.md)

### Q02: How many days do I have to return a product?
- Expected: returns_policy.md
- Retrieved: returns_policy_v1.3.md, returns_policy.md, damaged_or_wrong_items.md - hit@3: ✅
- Correct?: [ ]

> You have **14 days** from the date of purchase to return a product. (Source: returns_policy_v1.3.md)

### Q03: I paid by bank transfer. How long until I get my money back after I return an item?
- Expected: refunds.md
- Retrieved: returns_policy.md, refunds.md, returns_policy_v1.3.md - hit@3: ✅
- Correct?: [ ]

> If you paid by bank transfer, the refund will be sent to the same bank account within **7–10 business days after the return is approved** (i.e., after the item has been inspected). (Source: refunds.md)

### Q04: Do you deliver to Kuwait?
- Expected: shipping_and_delivery.md
- Retrieved: shipping_and_delivery.md, faq.md, stores_and_service_center.md - hit@3: ✅
- Correct?: [ ]

> No. NovaTech delivers **within Jordan only** and does not ship internationally. (Source: shipping_and_delivery.md)

### Q05: Can I return earbuds I opened if they work fine?
- Expected: returns_policy.md
- Retrieved: returns_policy.md, returns_policy_v1.3.md, refunds.md - hit@3: ✅
- Correct?: [ ]

> No. Once the hygiene seal on in‑ear headphones or earbuds is broken, they cannot be returned unless they are defective. (Source: returns_policy.md; also confirmed by returns_policy_v1.3.md).

### Q06: My order arrived broken. What should I do?
- Expected: damaged_or_wrong_items.md
- Retrieved: damaged_or_wrong_items.md, warranty.md, faq.md - hit@3: ✅
- Correct?: [ ]

> If your order arrived broken, you need to report the problem within **48 hours of delivery**.  
> 
> 1. Open **“My Orders” → “Report a problem”** (or call customer service).  
> 2. Provide:  
>    - Your order number  
>    - Clear photos of the broken item and its packaging  
> 
> After you report it, NovaTech will:  
> 
> 1. Arrange a free courier pickup within **2 business days**.  
> 2. Let you choose a **replacement** or a **full refund** (including any delivery fee).  
> 3. Ship the replacement as soon as the pickup is completed.  
> 
> (Source: damaged_or_wrong_items.md)

### Q07: How much is delivery to Irbid for a 40 JOD order, and how long does it take?
- Expected: shipping_and_delivery.md
- Retrieved: shipping_and_delivery.md, damaged_or_wrong_items.md, faq.md - hit@3: ✅
- Correct?: [ ]

> The delivery fee for a 40 JOD order to Irbid is **5 JOD**, and the standard delivery time is **2–3 business days**. (Source: shipping_and_delivery.md)

### Q08: Who is the CEO of NovaTech?
- Expected: (none - not answerable)
- Retrieved: returns_policy.md, returns_policy_v1.3.md, warranty.md - hit@3: n/a
- Correct?: [ ]

> The provided documents do not contain the answer to this question.

### Q09: Is my laptop battery covered for 2 years?
- Expected: warranty.md
- Retrieved: warranty.md, warranty.md, gift_cards.md - hit@3: ✅
- Correct?: [ ]

> No. Built‑in laptop batteries are covered for **12 months only**, even though the laptop itself has a 24‑month warranty. (Source: warranty.md)

### Q10: Do you offer a student discount?
- Expected: (none - not answerable)
- Retrieved: novapoints_loyalty.md, returns_policy.md, price_match.md - hit@3: n/a
- Correct?: [ ]

> The provided documents do not contain the answer to this question.

### Q11: Is the Irbid store open on Friday?
- Expected: stores_and_service_center.md
- Retrieved: stores_and_service_center.md, faq.md, returns_policy_v1.3.md - hit@3: ✅
- Correct?: [ ]

> No. The Irbid store is closed on Friday. (Source: stores_and_service_center.md)

### Q12: I'm a Gold member. I bought headphones 40 days ago and never opened them. Can I return them?
- Expected: novapoints_loyalty.md, returns_policy.md
- Retrieved: returns_policy.md, returns_policy_v1.3.md, refunds.md - hit@3: ✅
- Correct?: [ ]

> No. NovaTech’s Returns Policy (Version 1.3) allows products to be returned only **within 14 days of purchase** (returns_policy_v1.3.md). Since you bought the headphones 40 days ago, the return window has passed, so the items cannot be returned now.

## Task 5 best - chunk_size=500, overlap=50 (33 chunks) - hit@3 = 10/10

### Q01: How long is the warranty on a TV?
- Expected: warranty.md
- Retrieved: warranty.md, warranty.md, warranty.md - hit@3: ✅
- Correct?: [ ]

> The warranty for a TV is **24 months**. (Source: warranty.md)

### Q02: How many days do I have to return a product?
- Expected: returns_policy.md
- Retrieved: returns_policy.md, returns_policy_v1.3.md, returns_policy.md - hit@3: ✅
- Correct?: [ ]

> You have **30 days from the delivery date** to return most products. (Source: returns_policy.md)

### Q03: I paid by bank transfer. How long until I get my money back after I return an item?
- Expected: refunds.md
- Retrieved: returns_policy.md, refunds.md, refunds.md - hit@3: ✅
- Correct?: [ ]

> The provided documents do not contain the answer to this question. (Source: refunds.md)

### Q04: Do you deliver to Kuwait?
- Expected: shipping_and_delivery.md
- Retrieved: shipping_and_delivery.md, shipping_and_delivery.md, returns_policy_v1.3.md - hit@3: ✅
- Correct?: [ ]

> No. NovaTech delivers **within Jordan only** and does not ship internationally. (Source: shipping_and_delivery.md)

### Q05: Can I return earbuds I opened if they work fine?
- Expected: returns_policy.md
- Retrieved: returns_policy.md, returns_policy_v1.3.md, returns_policy.md - hit@3: ✅
- Correct?: [ ]

> No. Opened earbuds cannot be returned unless they are defective. Both the general policy and the current version of the returns policy list earbuds as non‑returnable once the hygiene seal is broken or the item is opened. (Source: returns_policy.md; returns_policy_v1.3.md)

### Q06: My order arrived broken. What should I do?
- Expected: damaged_or_wrong_items.md
- Retrieved: damaged_or_wrong_items.md, returns_policy_v1.3.md, warranty.md - hit@3: ✅
- Correct?: [ ]

> Report the problem within 48 hours of delivery. Use **“My Orders” → “Report a problem”** in the app or call customer service. Include:
> 
> - Your order number  
> - Clear photos of the damaged item and its packaging (and a photo of the label if it’s the wrong item)
> 
> (Source: damaged_or_wrong_items.md)

### Q07: How much is delivery to Irbid for a 40 JOD order, and how long does it take?
- Expected: shipping_and_delivery.md
- Retrieved: shipping_and_delivery.md, shipping_and_delivery.md, damaged_or_wrong_items.md - hit@3: ✅
- Correct?: [ ]

> The delivery fee for a 40 JOD order to Irbid is **5 JOD** (orders under 50 JOD cost 5 JOD outside Amman)【shipping_and_delivery.md】.  
> Standard delivery to Irbid takes **2–3 business days**【shipping_and_delivery.md】.

### Q08: Who is the CEO of NovaTech?
- Expected: (none - not answerable)
- Retrieved: returns_policy.md, returns_policy_v1.3.md, warranty.md - hit@3: n/a
- Correct?: [ ]

> The provided documents do not contain the answer to this question.

### Q09: Is my laptop battery covered for 2 years?
- Expected: warranty.md
- Retrieved: warranty.md, returns_policy.md, warranty.md - hit@3: ✅
- Correct?: [ ]

> No. Built‑in laptop batteries are covered for **12 months only**, even if the laptop itself has a longer warranty. (Source: warranty.md)

### Q10: Do you offer a student discount?
- Expected: (none - not answerable)
- Retrieved: novapoints_loyalty.md, novapoints_loyalty.md, returns_policy.md - hit@3: n/a
- Correct?: [ ]

> The provided documents do not contain the answer to this question.

### Q11: Is the Irbid store open on Friday?
- Expected: stores_and_service_center.md
- Retrieved: stores_and_service_center.md, faq.md, stores_and_service_center.md - hit@3: ✅
- Correct?: [ ]

> No. The Irbid store is closed on Friday. (Source: stores_and_service_center.md)

### Q12: I'm a Gold member. I bought headphones 40 days ago and never opened them. Can I return them?
- Expected: novapoints_loyalty.md, returns_policy.md
- Retrieved: returns_policy.md, returns_policy_v1.3.md, returns_policy.md - hit@3: ✅
- Correct?: [ ]

> No. NovaTech’s returns policy allows products to be returned only within **14 days of purchase** (returns_policy_v1.3.md). Since your headphones were bought **40 days ago**, the return window has passed, so they cannot be returned.
