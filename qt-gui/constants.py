import datetime

TITLE = "视频下载器(yt-dlp QtGUI)"
VERSION = "V2.1.0"
LAST_EDIT_DATE = datetime.datetime(2023, 6, 2).strftime('%x')

# 用户配置
CONFIG_YML = './configs.yml'
UI = 'yt-dlp-simple-gui.ui'
ABOUT_UI = 'about.ui'

# 一些ComboBox列表
SUBTITLE_FORMAT_LIST = ["best", "srt", "sub", "ssa", "smi", "vtt", "sub", "ass", "txt", "psb", "txt", "ttml", "srv", "xml", "json"]
SUB_LANGS = ['auto', 'sq', 'aa', 'akk', 'ak', 'ar', 'arc', 'am', 'as', 'az', 'ee', 'ay', 'ga', 'et', 'oc', 'or', 'om', 'ba', 'eu', 'be', 'bm', 'bg', 'nd', 'nso', 'bi', 'is', 'pl', 'bs', 'fa', 'fa-AF', 'fa-IR', 'brx', 'bh', 'br', 'bo', 'tn', 'ts', 'tt', 'da', 'tok', 'de', 'de-AT', 'de-DE', 'de-CH', 'doi', 'ru', 'ru-Latn', 'fo', 'fr', 'fr-BE', 'fr-FR', 'fr-CA', 'fr-CH', 'sa', 'fil', 'fj', 'fi', 'ff', 'km', 'kl', 'ka', 'gu', 'guz', 'gn', 'ie', 'ia', 'kk', 'ht', 'ko', 'ha', 'nl', 'nl-BE', 'nl-NL', 'mxp', 'ki', 'gl', 'ca', 'cs', 'kln', 'kam', 'kn', 'ky', 'cop', 'xh', 'co', 'cr', 'tlh', 'hr', 'qu', 'ks', 'hak', 'hak-TW', 'kok', 'ku', 'lad', 'la', 'lv', 'lo', 'lt', 'ln', 'rn', 'luo', 'lg', 'lb', 'rw', 'luy', 'lu', 'ro', 'mo', 'rm', 'mt', 'mr', 'mg', 'ml', 'ms', 'mk', 'mas', 'mai', 'mni', 'mi', 'mer', 'mn', 'mn-Mong', 'bn', 'lus', 'my', 'nan', 'nan-TW', 'nv', 'nr', 'af', 'st', 'na', 'ne', 'pcm', 'no', 'pap', 'pa', 'pt', 'pt-BR', 'pt-PT', 'ps', 'tw', 'cho', 'chr', 'ja', 'sv', 'sc', 'sm', 'sh', 'sr', 'sr-Latn', 'sr-Cyrl', 'sg', 'sat', 'si', 'sn', 'eo', 'sk', 'sl', 'ss', 'sw', 'gd', 'so', 'tl', 'tg', 'te', 'ta', 'th', 'to', 'ti', 'tr', 'tk', 'tpi', 'wal', 'cy', 'ug', 've', 'vo', 'wo', 'ur', 'uk', 'uz', 'es', 'es-419', 'es-US', 'es-MX', 'es-ES', 'fy', 'scn', 'iw', 'el', 'ho', 'haw', 'sd', 'hu', 'su', 'hy', 'ig', 'ik', 'it', 'yi', 'iu', 'hi', 'hi-Latn', 'id', 'en', 'en-IE', 'en-CA', 'en-US', 'en-IN', 'en-GB', 'yo', 'yue', 'yue-HK', 'vi', 'jv', 'zh', 'zh-Hant', 'zh-Hans', 'zh-TW', 'zh-HK', 'zh-SG', 'zh-CN', 'dz', 'zu', 'ase', 'bgc', 'sdp', 'vro']
TRANS_DEST_LANGS = ['af', 'ak', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bn', 'eu', 'be', 'bho', 'bs', 'bg', 'my', 'ca', 'ceb', 'zh-Hans', 'zh-Hant', 'co', 'hr', 'cs', 'da', 'dv', 'nl', 'en', 'eo', 'et', 'ee', 'fil', 'fi', 'fr', 'gl', 'lg', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'kri', 'ku', 'ky', 'lo', 'la', 'lv', 'ln', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'ne', 'nso', 'no', 'ny', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'sr', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'st', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'fy', 'xh', 'yi', 'yo', 'zu']
VIDEO_QUALITY_LIST = ["144", "240", "360", "480", "720", "1080", "1440", "2160", "4320"]
VIDEO_FORMAT_LIST = ["avi", "flv", "mkv", "mov", "mp4", "webm"]    
AUDIO_QUALITY_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
AUDIO_FORMAT_LIST = ["best", "aac", "alac", "flac", "m4a", "mp3", "opus", "vorbis", "wav"] 
BROWSER_LIST = ["brave", "chrome", "chromium", "edge", "firefox", "opera", "safari", "vivaldi"]
RECODE_VIDEO_LIST = ["avi", "flv", "gif", "mkv", "mov", "mp4", "webm", "aac", "aiff", "alac", "flac", "m4a",  "mka", "mp3", "ogg", "opus", "vorbis", "wav"]

CHECKBOX_PARAMETER = {
    "needs_translation_checkbox" : 'needs_translation',
    "embed_sub_checkbox": 'embed_sub',
    "live_chat_subs_checkbox": 'live_chat_subs',
    "all_subtitles_checkbox": 'download_all_subs',
    "recode_video_checkbox": 'recode_video',
    "import_cookies_from_browser_checkbox": 'import_cookies_from_browser', 
    "only_download_audio_checkbox": 'only_download_audio', 
    "download_all_playlist_checkbox": 'download_all_playlist',
    "download_thumbnail_checkbox": 'download_thumbnail',
}
COMBOBOX_PARAMETER = {
    "subtitle_format_menu": 'subtitle_format',
    "subtitle_langs_menu": 'subtitle_langs',
    "translation_dest_lang_menu": 'subtitle_trans_dest_lang',
    "video_quality_menu": 'video_quality',
    "video_format_menu": 'video_format',
    "audio_quality_menu": 'audio_quality',
    "audio_format_menu": 'audio_format',
    "browser_menu": 'browser_to_import_cookie',
    "recode_video_menu": 'recode_video_format',
}

COMBOBOX_INITS = {
    'subtitle_format': 'srt',
    'subtitle_langs': 'zh-CN',
    'subtitle_trans_dest_lang': 'en',
    'video_quality': '720',
    'video_format': 'mp4',
    'audio_quality': '0',
    'audio_format': 'm4a',
    'browser_to_import_cookie': 'chrome',
    'recode_video_format': 'mp4',
}

LANG_ACTION = {
    "actionSimplifiedChinese" : 'zh_CN',
    "actionEnglish" : 'en',
    "actionTraditionalChinese" : 'zh_TW',
}

TRANSLATE = {
    'zh_CN': {
        'downloaded_label': '已下载',
        'total_label': '总大小',
        'total_bytes_estimate_label' : '预估大小',
        'elapsed_label': '历时',
        'eta_label': '剩余时间',
        'speed_label': '速度',
        'unknown': '未知',
        'notice': '提示',
        'please_enter_link' : '请输入视频链接',
        'choose_folder': '选择保存文件夹',
        'success': '成功',
        'open_folder?' : "下载完成!\n是否要打开文件夹?",
        'error' : '错误',
        'ContentTooShortError' : '内容太短',
        'DownloadError' : '下载错误',
        'EntryNotInPlaylist' : '播放列表中无此条目',
        'ExistingVideoReached' : '已达到现有视频数目上限',
        'GeoRestrictedError' : '地理位置受限',
        'ExtractorError' : '提取器错误',
        'MaxDownloadsReached' : '已达最大下载数',
        'PostProcessingError' : '后处理错误',
        'SameFileError' : '相同文件',
        'UnavailableVideoError' : '视频不可用',
    },
    'en': {
        'downloaded_label': 'Downloaded',
        'total_label': 'Total',
        'total_bytes_estimate_label' : 'Estimate size',
        'elapsed_label' : 'Elapsed',
        'eta_label': 'ETA',
        'speed_label': 'Speed',
        'unknown': 'Unknown',
        'notice': 'Notice',
        'please_enter_link' : 'Please enter video link',
        'choose_folder': 'Select save folder',
        'success': 'Success',
        'open_folder?' : "Download Complete!\nDo you want to open the folder?",
        'error' : 'Error',
        'ContentTooShortError' : 'Content too short',
        'DownloadError' : 'Download Error',
        'EntryNotInPlaylist' : 'There is no such entry in the playlist',
        'ExistingVideoReached' : 'The maximum number of existing videos has been reached',
        'GeoRestrictedError' : 'GeoRestricted',
        'ExtractorError' : 'Extractor Error',
        'MaxDownloadsReached' : 'The maximum number of downloads has been reached',
        'PostProcessingError' : 'PostProcessing Error',
        'SameFileError' : 'Same File Error',
        'UnavailableVideoError' : 'Video is unavailable',
    },
    'zh_TW':{
        'downloaded_label': '已下載',
        'total_label': '總大小',
        'total_bytes_estimate_label': '預估檔案大小',
        'elapsed_label' : '歷時',
        'eta_label' : '剩餘時長',
        'speed_label': '速度',
        'unknown': '未知',
        'notice': '提醒',
        'please_enter_link' : '請輸入影片連結',
        'choose_folder': '選擇儲存資料夾',
        'success': '成功',
        'open_folder?' : "下載完成!\n是否要打開資料夾?",
        'error' : '錯誤',
        'ContentTooShortError' : '內容太短',
        'DownloadError' : '下載錯誤',
        'EntryNotInPlaylist' : '播放清單中無此條目',
        'ExistingVideoReached' : '已達到現有影片數目上限',
        'GeoRestrictedError' : '地理位置受限',
        'ExtractorError' : '提取器錯誤',
        'MaxDownloadsReached' : '已達最大下載數',
        'PostProcessingError' : '後處理錯誤',
        'SameFileError' : '相同檔錯誤',
        'UnavailableVideoError' : '影片不可用',
    },
}