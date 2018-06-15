def getTagColor(tag_name=""):
    return "red"


def jinja2_tag_color_zipper(dummy, arg1, arg2):
    """
    Args:
        dummy (TYPE): not matter
        arg1 (list of tags): this is list of tags created by pelican, no need
                             to parse it again 
        arg2 (str): this is a str represent tag colors sepertaed with `,`
                    should split by `,` then zip it with `arg1`
    
    Returns:
        TYPE: Description
    """
    arg2 = arg2.split(',')
    return zip(arg1, arg2)

def convert_to_jalali_date(value, format="%x"):
    from khayyam import JalaliDatetime
    jd=JalaliDatetime(value)
    return jd.strftime(format)