from parser import parser

def interpret(code):
    try:
        parser.parse(code)
        return "✅ تم تنفيذ الكود بنجاح!"
    except Exception as e:
        return f"⚠️ خطأ: {e}"
