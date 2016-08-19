#!/usr/bin/env bash
py.test \
    --platform_name='iOS' \
    --platform_version='9.3' \
    --device_name='iPhone 6 Plus' \
    --device_udid='23f7c26d8cd5097555991644f657ba515401ebac' \
    --bundle_id='cn.com.10jqka.iHexinFee' \
    --html=report.html \
    --rerun 0 \
    --junitxml=report.xml \
    --auto_acceptAlerts='true'


# 57e95712fdd52a1fce030ed46808f1a98e9b2f5e