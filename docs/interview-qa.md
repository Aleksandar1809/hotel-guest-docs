# Interview Q&A: AI adoption, answered from a real hotel project

Context: six AI document generators in daily use at a 5★ Superior resort in Tyrol, Austria (menu, kids' menu, wine list, weekly programme, kids' programme, daily morning newsletter; up to DE, EN, FR, IT).

### 1. How accurate is it? How do you stop the AI from making things up?
Accuracy is designed in, not hoped for. The AI checks the German source first and gives an explicit verdict before translating. Terms come from approved house tables, and layouts come from code, so they are identical every day. The rule "never invent facts" is explicit: if the sommelier forgets a vintage, the system asks instead of guessing. Staff still review the result, and the hotel's French reviewer's corrections become permanent rules.

### 2. What about data privacy?
The generators only see menus, wine sheets and activity schedules, never guest data. The system runs on the hotel's own accounts. For my portfolio I rebuilt everything with a fictional hotel and removed every name, price and contact detail. Choosing what *not* to feed the AI is the first privacy control.

### 3. What does it cost, and what is the return?
One Claude Pro subscription, about €20 per month. It saves about 2 staff hours per day, 7 days a week, about 60 hours per month. Even at a modest hourly rate, that pays for the tool many times over, and the staff spend those hours on guests instead.

### 4. How did you get staff to actually use it?
The workflow mirrors what they already did: paste what the kitchen or sommelier sends, get the finished documents back. Answers are short, with no AI chatter, so it feels like a tool, not a chatbot. The owners and a part-time colleague were trained, and it now runs without me.

### 5. Aren't you locked into one AI vendor?
No. The rules, term tables and templates are plain files, and an exportable backup (~130 MB) lets the system be restored or moved to another AI provider. The newsletter even has a written spec so it can be rebuilt in a classic layout tool. The value sits in the hotel's rules, not in the vendor.

### 6. What happens when the person who built it leaves?
That was a design goal from the start. It runs on the hotel's own accounts, the owners and a part-time colleague were trained, and the backup includes a restore guide. It already runs without me.

### 7. Why not just use a translation tool?
Translation is only one step. The real work is checking a handwritten German menu, completing an incomplete wine list, applying a house style (one "avec" per dish in French, fixed category names, British spelling), and delivering print-ready files in a fixed layout. Each generator was refined through many iterations to do all of that with precise output at minimal token use.

### 8. How do you keep quality from drifting over time?
Three habits. Every correction from a reviewer is turned into a written rule, and conflicting corrections are flagged, not silently resolved. Changes after delivery return only the affected lines, so nothing else can shift. Each generator has one source of truth (one briefing, one term table) instead of rules scattered across chat history.
