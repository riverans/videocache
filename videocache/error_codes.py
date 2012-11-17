#!/usr/bin/env python
#
# (C) Copyright White Magnet Software Private Limited
# Company Website : http://whitemagnet.com/
# Product Website : http://cachevideos.com/
#

__author__ = """Kulbir Saini <saini@saini.co.in>"""
__docformat__ = 'plaintext'

CACHE_URL_ERR = 'CACHE_URL_ERR'
WEBSITE_OPTIONS_ERR = 'WEBSITE_OPTIONS_ERR'
CACHE_DIR_BUILD_ERR = 'CACHE_DIR_BUILD_ERR'
RPC_CONNECT_WARN = 'RPC_CONNECT_WARN'
RPC_CONNECT_ERR = 'RPC_CONNECT_ERR'
RPC_CONNECT = 'RPC_CONNECT'
VIDEOCACHE_START_ERR = 'VIDEOCACHE_START_ERR'
VIDEOCACHE_START_WARN = 'VIDEOCACHE_START_WARN'
VIDEOCACHE_START = 'VIDEOCACHE_START'
VIDEOCACHE_RUNTIME_ERR = 'VIDEOCACHE_RUNTIME_ERR'
INPUT_WARN = 'INPUT_WARN'
HTTP_METHOD_WARN = 'HTTP_METHOD_WARN'
URL_WARN = 'URL_WARN'
INPUT_PARSE_ERR = 'INPUT_PARSE_ERR'
URL_ERR = 'URL_ERR'
URL_HIT = 'URL_HIT'
CACHE_MISS = 'CACHE_MISS'
CACHE_HIT = 'CACHE_HIT'
WRITEBACK_ERR = 'WRITEBACK_ERR'
VIDEOCACHE_EXIT = 'VIDEOCACHE_EXIT'
LOCAL_POOL_LOCK_ERR = 'LOCAL_POOL_LOCK_ERR'
FORK_1_FAILED = 'FORK_1_FAILED'
FORK_2_FAILED = 'FORK_2_FAILED'
PID_NOT_FOUND = 'PID_NOT_FOUND'
VIDEO_POOL_SERVER_START = 'VIDEO_POOL_SERVER_START'
VIDEO_POOL_SERVER_START_ERR = 'VIDEO_POOL_SERVER_START_ERR'
VIDEO_SUBMIT = 'VIDEO_SUBMIT'
VIDEO_SUBMIT_ERR = 'VIDEO_SUBMIT_ERR'
VIDEO_SUBMIT_FAIL = 'VIDEO_SUBMIT_FAIL'
VIDEO_SUBMIT_WARN = 'VIDEO_SUBMIT_WARN'
VIDEO_SYNC_START = 'VIDEO_SYNC_START'
VIDEO_SYNC_STOP = 'VIDEO_SYNC_STOP'
VIDEOS_RECEIVED = 'VIDEOS_RECEIVED'
CACHE_THREAD_START = 'CACHE_THREAD_START'
CACHE_THREAD_REMOVE = 'CACHE_THREAD_REMOVE'
CACHE_THREAD_REMOVE_ERR = 'CACHE_THREAD_REMOVE_ERR'
VIDEO_SCHEDULE_ERR = 'VIDEO_SCHEDULE_ERR'
CACHE_THREAD_SCHEDULER_START = 'CACHE_THREAD_SCHEDULER_START'
CACHE_THREAD_SCHEDULE_WARN = 'CACHE_THREAD_SCHEDULE_WARN'
CACHE_THREAD_SCHEDULER_START = 'CACHE_THREAD_SCHEDULER_START'
CACHE_THREAD_SCHEDULE_FAIL = 'CACHE_THREAD_SCHEDULE_WARN'
VIDEO_INFO_ERR = 'VIDEO_INFO_ERR'
VIDEO_EXISTS = 'VIDEO_EXISTS'
CACHE_DIR_FULL = 'CACHE_DIR_FULL'
CACHE_DIR_ERR = 'CACHE_DIR_ERR'
CACHE_HTTP_ERR = 'CACHE_HTTP_ERR'
CACHE_ERR = 'CACHE_ERR'
VIDEO_INFO2_ERR = 'VIDEO_INFO2_ERR'
VIDEO_CACHED = 'VIDEO_CACHED'
URL_CACHE_ERR = 'URL_CACHE_ERR'
VIDEO_PAGE_ERR = 'VIDEO_PAGE_ERR'
VIDEO_INFO_FETCH_ERR = 'VIDEO_INFO_FETCH_ERR'
ALTERNATE_VIDEO_ID_ERROR = 'ALTERNATE_VIDEO_ID_ERROR'
VIDEO_URL_ERR = 'VIDEO_URL_ERR'
VIDEO_LINK_ERR = 'VIDEO_LINK_ERR'
VIDEO_SEARCH_WARN = 'VIDEO_SEARCH_WARN'
VIDEO_SIZE_NOT_SUPPLIED = 'VIDEO_SIZE_NOT_SUPPLIED'
VIDEO_TOO_LARGE = 'VIDEO_TOO_LARGE'
VIDEO_TOO_SMALL = 'VIDEO_TOO_SMALL'
CONNECTION_INFO_ERR = 'CONNECTION_INFO_ERR'
QUEUE_LOAD_WARN = 'QUEUE_LOAD_WARN'
QUEUE_DUMP_WARN = 'QUEUE_DUMP_WARN'
QUEUE_LOAD = 'QUEUE_LOAD'
QUEUE_INCOMPATIBLE = 'QUEUE_INCOMPATIBLE'
CACHE_DIR_CHECK = 'CACHE_DIR_CHECK'
CACHE_DIR_NOT_FOUND = 'CACHE_DIR_NOT_FOUND'
PARTIAL_CACHE_ERR = 'PARTIAL_CACHE_ERR'
VIEW_COUNT_LOW = 'VIEW_COUNT_LOW'
CACHE_PERIOD_WARN = 'CACHE_PERIOD_WARN'
CACHE_HOST_ERR = 'CACHE_HOST_ERR'
CACHE_HOST_WARN = 'CACHE_HOST_WARN'
APACHE_CONNECT_ERR = 'APACHE_CONNECT_ERR'
APACHE_404_ERR = 'APACHE_404_ERR'
APACHE_403_ERR = 'APACHE_403_ERR'
QUEUE_FLUSH = 'QUEUE_FLUSH'
QUEUE_FLUSH_ERR = 'QUEUE_FLUSH_ERR'
VIDEO_ID_ENCODING = 'VIDEO_ID_ENCODING'
DAILYMOTION_FF_ERR = 'DAILYMOTION_FF_ERR'
FILELIST_BUILD_START = 'FILELIST_BUILD_START'
FILELIST_BUILD_FINISH = 'FILELIST_BUILD_FINISH'
FILELIST_BUILD_ERR = 'FILELIST_BUILD_ERR'
CLEANUP_INITIATED = 'CLEANUP_INITIATED'
CLEANUP_COMPLETED = 'CLEANUP_COMPLETED'
CLEANER_START = 'CLEANER_START'
CLEANER_FINISH = 'CLEANER_FINISH'
CLEANER_ERR = 'CLEANER_ERR'
CLEANER_OUT_OF_JUNK = 'CLEANER_OUT_OF_JUNK'
VIDEO_PURGED = 'VIDEO_PURGED'
VIDEO_PURGE_WARN = 'VIDEO_PURGE_WARN'
VIDEO_PURGE_ERR = 'VIDEO_PURGE_ERR'
LOCAL_PROXY_NOT_SPECIFIED = 'LOCAL_PROXY_NOT_SPECIFIED'
STORE_LOG_OPEN_ERR = 'STORE_LOG_OPEN_ERR'
STORE_LOG_NOT_FOUND = 'STORE_LOG_NOT_FOUND'
STORE_LOG_URL_HIT = 'STORE_LOG_URL_HIT'
STORE_LOG_CACHE_ERR = 'STORE_LOG_CACHE_ERR'
STORE_LOG_READ_ERR = 'STORE_LOG_READ_ERR'
STORE_LOG_WATCH_START = 'STORE_LOG_WATCH_START'
CACHE_IN_PROGRESS = 'CACHE_IN_PROGRESS'
STORE_LOG_URL_HIT_CONFIRMED = 'STORE_LOG_URL_HIT_CONFIRMED'
STORE_LOG_URL_HIT_CONFIRMATION_FAILED = 'STORE_LOG_URL_HIT_CONFIRMATION_FAILED'
STORE_LOG_CHECK_ERR = 'STORE_LOG_CHECK_ERR'
STORE_LOG_NOT_MONITORED = 'STORE_LOG_NOT_MONITORED'
VIDEO_ID_NOT_FOUND = 'VIDEO_ID_NOT_FOUND'
FORMAT_INFO_NOT_FOUND = 'FORMAT_INFO_NOT_FOUND'
ALL_QUEUED_FORMATS_CACHED = 'ALL_QUEUED_FORMATS_CACHED'
FILEDB_REPORT_ERR = 'FILEDB_REPORT_ERR'
