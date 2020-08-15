#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


#======
# name: tools.py
# date: 2019SEP21
#       2019SEP17
#       2019SEP06
#       2019AUG11
#       2016FEB03
# prog: pr
# desc: tools for image processing
# urls: 
#       datetime
#       <http://strftime.org/>
#       <http://pleac.sourceforge.net/pleac_python/datesandtimes.html>
#======


import sys
import glob
import time
import os.path
import datetime


#------ debug start ---------
DEBUG = False
def msg(msg, is_debug=DEBUG):
    if is_debug: print("> {}".format(msg))
#------ debug end ---------


#------ date time start -----
#------
# desc: datetime string in YYYY MMM DD HH MM SS format
#       and display as "YYYYMMMDDTHH:MM.SS", components
#       are the following:
#       YYYY = %Y  -- full 4 digit year
#       MMM  = %b  -- truncated month, UC
#       DD   = %d  -- day, zero padded
#       HH   = %H  -- 24 hour, zero padded
#       MM   = %M  -- minute, zero padded
#       SS   = %S  -- second, zero padded
#------
DTF_YYYYMMMDDTHHMMSS = "%Y%b%dT%H:%M.%S"
DTF_YYYYMMMDDTHHMMSS_FN = "%Y%b%d%H%M%S"

#---------
# dt_date2str: convert datetime to string format for filenames
#  
# desc: 2019SEP21 removed dot due to truncation on flickr        
#---------
def dt_date2str(dt, dt_format=DTF_YYYYMMMDDTHHMMSS):
    """convert a valid date time to a string format"""
    if dt_format:
        dts = dt.strftime(dt_format)
        time_delta = format(time.process_time(), '.3f')    # remove dot
        dts = "{}{}".format(dts, time_delta)              # remove dot
        dts = dts.upper()
        return dts 
    else:
        return ""
#---------
# dt_get_now: WARNING have set to local time not UTC
#---------
def dt_get_now(is_utc=False):
    """return current, now  date time"""
    if is_utc:
        return datetime.datetime.utcnow()
    else:
        return datetime.datetime.now()
def dt2epoch(dt):
    """
    given datetime object, return epoch
    be aware of the differences b/w now 
    utc_now (local time and UTC time)
    """
    e = time.mktime(dt.timetuple())
    return e
def dt_build_date(yyyy, mmm, dd, hh=0, mm=0, ss=0):
    """
    build datetime obj from year, month, day, hour, min, seconds 
    """
    dt = datetime.datetime(yyyy, mmm, dd, hh, mm, ss)
    return dt
def dt_build_fn(ext):
    """build extention type, build filename in date format"""
    dt = dt_get_now()
    fn = dt_date2str(dt, dt_format=DTF_YYYYMMMDDTHHMMSS_FN)
    msg("fn <{}.{}>".format(fn, ext)) 
    return "{}.{}".format(fn, ext)
def dt_build_fn_jpg():
    return dt_build_fn(ext='jpg')
def dt_build_fn_png():
    return dt_build_fn(ext='png')


#------ date time end ------

#------ filenames start ------
def get_filenames(filepathdirectory, file_type="*.*"):
    """
    given a valid filepath, gather all 
    the files in that directory as a list
    by globbing them using glob.glob. Use
    file_type to restrict or wild-card the 
    types of files to select.
    """
    fpd = filepathdirectory
    msg("tools.get_filenames.filepath <{}>".format(fpd))

    if os.path.isdir(fpd):
       fpn = os.path.join(fpd, file_type)
       files = glob.glob(fpn)

       msg("tools.get_filenames.fpn <{}>".format(fpn))
       msg("tools.get_filenames <{}>".format(files))
 
       return files
    else:
       return []
def get_fn_jpg(filepath):
    lower_fn = get_filenames(filepath, "*.jpg")
    upper_fn = get_filenames(filepath, "*.JPG")
    fn = lower_fn + upper_fn
    msg("fn <{}>".format(fn))
    return fn
def get_fn_jpeg(filepath):
    return get_filenames(filepath, "*.jpeg")
def get_fn_png(filepath):
    lower_fn = get_filenames(filepath, "*.png")
    upper_fn = get_filenames(filepath, "*.PNG")
    fn = lower_fn + upper_fn
    msg("fn <{}>".format(fn))
    return fn 
#---------
# name: filepath2title:
# desc: convert filepath (unix) to a filename
#                 use os.path.basename to extract info
# rets: filepath, filename
#---------
def filepath2title(fpn):
    """
    WARNING: IF THINGS ARE GOING TO FAIL, ITS MOST LIKELY HERE
    FIXME. REMOVE THE SPLITTING OF FILES LOOKING FOR EXT.

    convert filepath (unix) to a filename use os.path.basename 
    to extract info

      eg: convert from /some/filepath/filename.jpg
                  to   filename
          HACK add     filename + '.00'
    """
    msg("filepath2title")
    if fpn:
        fp = os.path.dirname(fpn)
        original_fp = fp
        fp = fp.replace(" ","-")
        
        title = os.path.basename(fpn)
        original_title = title
        e = title.split('.')

        # Oh bugger, dots in the file, 
        # grab the last one, thats the ext.
        if len(e) > 1:
            ext = e[len(e)-1]

        title = title.split(".{}".format(ext))
        new_t = title[0]
        new_t = new_t.replace(" ","-")
        title = new_t.replace(".","-")

        msg("title <{}> ext <{}>".format(title, ext))

        new_title = "{}.{}".format(title, ext)

        # yyyymmmddhh.00.jpg OR some_filename.jpg?
        #if len(title) > 1: 
        #    t = "{}.{}".format(title[0], title[1])
        #else:
        #    t = "{}".format(title[0])
        msg("fp <{}> title <{}>".format(fp, original_title))

        # filepath, filename title
        return [original_fp, original_title]
    else:
        return ""
#------ filenames end ------

def main():
    """cli entry point"""
    pass

#----- main cli entry point ------
if __name__ == "__main__":
    main()


## vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab

