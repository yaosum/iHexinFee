#!/usr/bin/env bash
py.test \
    --platform_name='iOS' \
    --platform_version='9.3' \
    --device_name='iPhone 6' \
    --device_udid='57e95712fdd52a1fce030ed46808f1a98e9b2f5e' \
    --bundle_id='cn.com.10jqka.iHexinFee' \
    --html=report.html \
    --rerun 0 \
    --junitxml=report.xml

