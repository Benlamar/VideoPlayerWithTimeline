from PySide6.QtMultimedia import  QMediaFormat

def get_supported_mime_types():
    result = []
    for f in QMediaFormat().supportedFileFormats(QMediaFormat.Decode):
        mime_type = QMediaFormat(f).mimeType()
        result.append(mime_type.name())
    return result

# def hhmmss(ms):
#     # s = 1000, # m = 60000, # h = 360000
#     h, r = divmod(ms, 36000)
#     m, r = divmod(r, 60000)
#     s, _ = divmod(r, 1000)
#     return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))

def convert_milliseconds(ms):
    total_secs = int(ms) // 1000
    # Convert total seconds to hours, minutes, and remaining seconds
    hours = total_secs // 3600
    mins = (total_secs % 3600) // 60
    secs = total_secs % 60
    
    # Use string formatting to ensure two digits for each unit of time
    return f"{hours:02d}:{mins:02d}:{secs:02d}"
