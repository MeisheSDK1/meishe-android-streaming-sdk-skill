# Demo Simple Snippets - Captions Stickers

These method-level simple snippets are compressed from the Android demo source.
They preserve reusable SDK call sequences and relative provenance labels, not full demo activities or proprietary runtime assets.

Read when: timeline/clip captions, compound captions, caption spans, animated stickers, sticker/caption packages, text styles, and keyframe editing.

Use `rg` in this file for an API class, method name, source label, or snippet id before loading unrelated sections.

<!-- BEGIN GENERATED CONTENTS -->
## Contents

- [captions-stickers-001 onScaleAndRotate](#captions-stickers-001-onscaleandrotate)
- [captions-stickers-002 deleteCaptionOrSticker](#captions-stickers-002-deletecaptionorsticker)
- [captions-stickers-003 deleteCaptionOrSticker](#captions-stickers-003-deletecaptionorsticker)
- [captions-stickers-004 deleteCaptionOrSticker](#captions-stickers-004-deletecaptionorsticker)
- [captions-stickers-005 deleteCaptionOrSticker](#captions-stickers-005-deletecaptionorsticker)
- [captions-stickers-006 checkSelectCaption](#captions-stickers-006-checkselectcaption)
- [captions-stickers-007 getCaptionList](#captions-stickers-007-getcaptionlist)
- [captions-stickers-008 getCaptionList](#captions-stickers-008-getcaptionlist)
- [captions-stickers-009 checkSelectByAttachment](#captions-stickers-009-checkselectbyattachment)
- [captions-stickers-010 checkSelectByAttachment](#captions-stickers-010-checkselectbyattachment)
- [captions-stickers-011 initData](#captions-stickers-011-initdata)
- [captions-stickers-012 seekTimeline](#captions-stickers-012-seektimeline)
- [captions-stickers-013 OnRightTextClick](#captions-stickers-013-onrighttextclick)
- [captions-stickers-014 playbackTimeline](#captions-stickers-014-playbacktimeline)
- [captions-stickers-015 seekTimeline](#captions-stickers-015-seektimeline)
- [captions-stickers-016 initRootView](#captions-stickers-016-initrootview)
- [captions-stickers-017 initListener](#captions-stickers-017-initlistener)
- [captions-stickers-018 onProgressChanged](#captions-stickers-018-onprogresschanged)
- [captions-stickers-019 onScrollX](#captions-stickers-019-onscrollx)
- [captions-stickers-020 playBackEOF](#captions-stickers-020-playbackeof)
- [captions-stickers-021 playStopped](#captions-stickers-021-playstopped)
- [captions-stickers-022 streamingEngineStateChanged](#captions-stickers-022-streamingenginestatechanged)
- [captions-stickers-023 updateCaptionControlPoint](#captions-stickers-023-updatecaptioncontrolpoint)
- [captions-stickers-024 updateCaptionControlPoint](#captions-stickers-024-updatecaptioncontrolpoint)
- [captions-stickers-025 updateCaptionRelativeView](#captions-stickers-025-updatecaptionrelativeview)
- [captions-stickers-026 generateKeyFrameInfo](#captions-stickers-026-generatekeyframeinfo)
- [captions-stickers-027 onClick](#captions-stickers-027-onclick)
- [captions-stickers-028 selectCaptionByZVal](#captions-stickers-028-selectcaptionbyzval)
- [captions-stickers-029 selectCaptionByZVal](#captions-stickers-029-selectcaptionbyzval)
- [captions-stickers-030 playVideo](#captions-stickers-030-playvideo)
- [captions-stickers-031 getCurCaptionZVal](#captions-stickers-031-getcurcaptionzval)
- [captions-stickers-032 addCaption](#captions-stickers-032-addcaption)
- [captions-stickers-033 addTimeSpan](#captions-stickers-033-addtimespan)
- [captions-stickers-034 rebuildBezierData](#captions-stickers-034-rebuildbezierdata)
- [captions-stickers-035 rebuildBezierData](#captions-stickers-035-rebuildbezierdata)
- [captions-stickers-036 addAllTimeSpan](#captions-stickers-036-addalltimespan)
- [captions-stickers-037 addAllTimeSpan](#captions-stickers-037-addalltimespan)
- [captions-stickers-038 selectCaption](#captions-stickers-038-selectcaption)
- [captions-stickers-039 selectCaption](#captions-stickers-039-selectcaption)
- [captions-stickers-040 selectTimeSpan](#captions-stickers-040-selecttimespan)
- [captions-stickers-041 selectTimeSpan](#captions-stickers-041-selecttimespan)
- [captions-stickers-042 selectTimeSpan](#captions-stickers-042-selecttimespan)
- [captions-stickers-043 initTitle](#captions-stickers-043-inittitle)
- [captions-stickers-044 playBackEOF](#captions-stickers-044-playbackeof)
- [captions-stickers-045 onTextChanged](#captions-stickers-045-ontextchanged)
- [captions-stickers-046 fontDownloadFail](#captions-stickers-046-fontdownloadfail)
- [captions-stickers-047 updateCaptionPosition](#captions-stickers-047-updatecaptionposition)
- [captions-stickers-048 applyAssemblyCaption](#captions-stickers-048-applyassemblycaption)
- [captions-stickers-049 initCaptionStyleFragment](#captions-stickers-049-initcaptionstylefragment)
- [captions-stickers-050 initCaptionColorFragment](#captions-stickers-050-initcaptioncolorfragment)
- [captions-stickers-051 initCaptionOutlineFragment](#captions-stickers-051-initcaptionoutlinefragment)
- [captions-stickers-052 initCaptionBackgroundFragment](#captions-stickers-052-initcaptionbackgroundfragment)
- [captions-stickers-053 onFragmentLoadFinished](#captions-stickers-053-onfragmentloadfinished)
- [captions-stickers-054 onCaptionColor](#captions-stickers-054-oncaptioncolor)
- [captions-stickers-055 initCaptionLetterSpacingFragment](#captions-stickers-055-initcaptionletterspacingfragment)
- [captions-stickers-056 onSmallBtnClicked](#captions-stickers-056-onsmallbtnclicked)
- [captions-stickers-057 onStandardBtnClicked](#captions-stickers-057-onstandardbtnclicked)
- [captions-stickers-058 onMoreBtnClicked](#captions-stickers-058-onmorebtnclicked)
- [captions-stickers-059 onLargeBtnClicked](#captions-stickers-059-onlargebtnclicked)
- [captions-stickers-060 initCaptionFontSizeRatioFragment](#captions-stickers-060-initcaptionfontsizeratiofragment)
- [captions-stickers-061 initCaptionShadowFragment](#captions-stickers-061-initcaptionshadowfragment)
- [captions-stickers-062 onChangeShadow](#captions-stickers-062-onchangeshadow)
- [captions-stickers-063 seekTimeline](#captions-stickers-063-seektimeline)
- [captions-stickers-064 getCurCaptionZVal](#captions-stickers-064-getcurcaptionzval)
- [captions-stickers-065 setSpanValue](#captions-stickers-065-setspanvalue)
- [captions-stickers-066 changeOrRemoveSpanByType](#captions-stickers-066-changeorremovespanbytype)
- [captions-stickers-067 createSpanByType](#captions-stickers-067-createspanbytype)
- [captions-stickers-068 convertFontData](#captions-stickers-068-convertfontdata)
- [captions-stickers-069 convertFontData](#captions-stickers-069-convertfontdata)
- [captions-stickers-070 convertFontData](#captions-stickers-070-convertfontdata)
- [captions-stickers-071 initDrawRectListener](#captions-stickers-071-initdrawrectlistener)
- [captions-stickers-072 onScaleXandY](#captions-stickers-072-onscalexandy)
- [captions-stickers-073 onScaleXandY](#captions-stickers-073-onscalexandy)
- [captions-stickers-074 onAlignClick](#captions-stickers-074-onalignclick)
- [captions-stickers-075 onAlignClick](#captions-stickers-075-onalignclick)
- [captions-stickers-076 onOrientationChange](#captions-stickers-076-onorientationchange)
- [captions-stickers-077 onOrientationChange](#captions-stickers-077-onorientationchange)
- [captions-stickers-078 onOrientationChange](#captions-stickers-078-onorientationchange)
- [captions-stickers-079 onHorizontalFlipClick](#captions-stickers-079-onhorizontalflipclick)
- [captions-stickers-080 onHorizontalFlipClick](#captions-stickers-080-onhorizontalflipclick)
- [captions-stickers-081 updateThemeCaptionCoordinate](#captions-stickers-081-updatethemecaptioncoordinate)
- [captions-stickers-082 setCurCaption](#captions-stickers-082-setcurcaption)
- [captions-stickers-083 updateCaptionCoordinate](#captions-stickers-083-updatecaptioncoordinate)
- [captions-stickers-084 updateCaptionCoordinate](#captions-stickers-084-updatecaptioncoordinate)
- [captions-stickers-085 setCurCompoundCaption](#captions-stickers-085-setcurcompoundcaption)
- [captions-stickers-086 updateCompoundCaptionCoordinate](#captions-stickers-086-updatecompoundcaptioncoordinate)
- [captions-stickers-087 updateCompoundCaptionCoordinate](#captions-stickers-087-updatecompoundcaptioncoordinate)
- [captions-stickers-088 selectCompoundCaptionByHandClick](#captions-stickers-088-selectcompoundcaptionbyhandclick)
- [captions-stickers-089 selectCaptionByHandClick](#captions-stickers-089-selectcaptionbyhandclick)
- [captions-stickers-090 setRecording](#captions-stickers-090-setrecording)
- [captions-stickers-091 updateAnimateStickerCoordinate](#captions-stickers-091-updateanimatestickercoordinate)
- [captions-stickers-092 selectAnimateStickerByHandClick](#captions-stickers-092-selectanimatestickerbyhandclick)
- [captions-stickers-093 isSelectedCaption](#captions-stickers-093-isselectedcaption)
- [captions-stickers-094 isSelectedAnimateSticker](#captions-stickers-094-isselectedanimatesticker)
- [captions-stickers-095 initListener](#captions-stickers-095-initlistener)
- [captions-stickers-096 onTouch](#captions-stickers-096-ontouch)
- [captions-stickers-097 playBackEOF](#captions-stickers-097-playbackeof)
- [captions-stickers-098 streamingEngineStateChanged](#captions-stickers-098-streamingenginestatechanged)
- [captions-stickers-099 updateAllStickerPos](#captions-stickers-099-updateallstickerpos)
- [captions-stickers-100 updateAllStickerPos](#captions-stickers-100-updateallstickerpos)
- [captions-stickers-101 updateAllKeyFrameViewStatusWhenScroll](#captions-stickers-101-updateallkeyframeviewstatuswhenscroll)
- [captions-stickers-102 updateAllKeyFrameViewStatusWhenScroll](#captions-stickers-102-updateallkeyframeviewstatuswhenscroll)
- [captions-stickers-103 onClick](#captions-stickers-103-onclick)
- [captions-stickers-104 selectAnimateStickerByZVal](#captions-stickers-104-selectanimatestickerbyzval)
- [captions-stickers-105 applyAnimateSticker](#captions-stickers-105-applyanimatesticker)
- [captions-stickers-106 applyAnimateSticker](#captions-stickers-106-applyanimatesticker)
- [captions-stickers-107 applyAnimateSticker](#captions-stickers-107-applyanimatesticker)
- [captions-stickers-108 applyCustomAnimateSticker](#captions-stickers-108-applycustomanimatesticker)
- [captions-stickers-109 applyCustomAnimateSticker](#captions-stickers-109-applycustomanimatesticker)
- [captions-stickers-110 applyCustomAnimateSticker](#captions-stickers-110-applycustomanimatesticker)
- [captions-stickers-111 addTimeSpanAndPlayVideo](#captions-stickers-111-addtimespanandplayvideo)
- [captions-stickers-112 deleteCurStickerTimeSpan](#captions-stickers-112-deletecurstickertimespan)
- [captions-stickers-113 addTimeSpan](#captions-stickers-113-addtimespan)
- [captions-stickers-114 seekTimeline](#captions-stickers-114-seektimeline)
- [captions-stickers-115 addAllTimeSpan](#captions-stickers-115-addalltimespan)
- [captions-stickers-116 addAllTimeSpan](#captions-stickers-116-addalltimespan)
- [captions-stickers-117 selectAnimateSticker](#captions-stickers-117-selectanimatesticker)
- [captions-stickers-118 initMultiSequence](#captions-stickers-118-initmultisequence)
- [captions-stickers-119 playStopped](#captions-stickers-119-playstopped)
- [captions-stickers-120 playbackTimelinePosition](#captions-stickers-120-playbacktimelineposition)
- [captions-stickers-121 streamingEngineStateChanged](#captions-stickers-121-streamingenginestatechanged)
- [captions-stickers-122 selectSticker](#captions-stickers-122-selectsticker)
- [captions-stickers-123 initRootView](#captions-stickers-123-initrootview)
- [captions-stickers-124 initRootView](#captions-stickers-124-initrootview)
- [captions-stickers-125 onClick](#captions-stickers-125-onclick)
- [captions-stickers-126 playBackEOF](#captions-stickers-126-playbackeof)
- [captions-stickers-127 playStopped](#captions-stickers-127-playstopped)
- [captions-stickers-128 setCustomStickerImageSize](#captions-stickers-128-setcustomstickerimagesize)
- [captions-stickers-129 initCaptionColorList](#captions-stickers-129-initcaptioncolorlist)
- [captions-stickers-130 onTouch](#captions-stickers-130-ontouch)
- [captions-stickers-131 playBackEOF](#captions-stickers-131-playbackeof)
- [captions-stickers-132 streamingEngineStateChanged](#captions-stickers-132-streamingenginestatechanged)
- [captions-stickers-133 updateAllStickerPos](#captions-stickers-133-updateallstickerpos)
- [captions-stickers-134 updateAllStickerPos](#captions-stickers-134-updateallstickerpos)
- [captions-stickers-135 updateAllKeyFrameViewStatusWhenScroll](#captions-stickers-135-updateallkeyframeviewstatuswhenscroll)
- [captions-stickers-136 updateAllKeyFrameViewStatusWhenScroll](#captions-stickers-136-updateallkeyframeviewstatuswhenscroll)
- [captions-stickers-137 onClick](#captions-stickers-137-onclick)
- [captions-stickers-138 selectAnimateStickerByZVal](#captions-stickers-138-selectanimatestickerbyzval)
- [captions-stickers-139 applyAnimateSticker](#captions-stickers-139-applyanimatesticker)
- [captions-stickers-140 applyAnimateSticker](#captions-stickers-140-applyanimatesticker)
- [captions-stickers-141 applyAnimateSticker](#captions-stickers-141-applyanimatesticker)
- [captions-stickers-142 applyCustomAnimateSticker](#captions-stickers-142-applycustomanimatesticker)
- [captions-stickers-143 applyCustomAnimateSticker](#captions-stickers-143-applycustomanimatesticker)
- [captions-stickers-144 applyCustomAnimateSticker](#captions-stickers-144-applycustomanimatesticker)
- [captions-stickers-145 addTimeSpanAndPlayVideo](#captions-stickers-145-addtimespanandplayvideo)
- [captions-stickers-146 deleteCurStickerTimeSpan](#captions-stickers-146-deletecurstickertimespan)
- [captions-stickers-147 addTimeSpan](#captions-stickers-147-addtimespan)
- [captions-stickers-148 seekTimeline](#captions-stickers-148-seektimeline)
- [captions-stickers-149 addAllTimeSpan](#captions-stickers-149-addalltimespan)
- [captions-stickers-150 addAllTimeSpan](#captions-stickers-150-addalltimespan)
- [captions-stickers-151 selectAnimateSticker](#captions-stickers-151-selectanimatesticker)
- [captions-stickers-152 initMultiSequence](#captions-stickers-152-initmultisequence)
- [captions-stickers-153 playStopped](#captions-stickers-153-playstopped)
- [captions-stickers-154 playbackTimelinePosition](#captions-stickers-154-playbacktimelineposition)
- [captions-stickers-155 streamingEngineStateChanged](#captions-stickers-155-streamingenginestatechanged)
- [captions-stickers-156 selectSticker](#captions-stickers-156-selectsticker)
- [captions-stickers-157 playbackTimeline](#captions-stickers-157-playbacktimeline)
- [captions-stickers-158 seekTimeline](#captions-stickers-158-seektimeline)
- [captions-stickers-159 initRootView](#captions-stickers-159-initrootview)
- [captions-stickers-160 initListener](#captions-stickers-160-initlistener)
- [captions-stickers-161 initListener](#captions-stickers-161-initlistener)
- [captions-stickers-162 onProgressChanged](#captions-stickers-162-onprogresschanged)
- [captions-stickers-163 onScrollX](#captions-stickers-163-onscrollx)
- [captions-stickers-164 onTouch](#captions-stickers-164-ontouch)
- [captions-stickers-165 playBackEOF](#captions-stickers-165-playbackeof)
- [captions-stickers-166 playStopped](#captions-stickers-166-playstopped)
- [captions-stickers-167 streamingEngineStateChanged](#captions-stickers-167-streamingenginestatechanged)
- [captions-stickers-168 updateCaptionControlPoint](#captions-stickers-168-updatecaptioncontrolpoint)
- [captions-stickers-169 updateCaptionControlPoint](#captions-stickers-169-updatecaptioncontrolpoint)
- [captions-stickers-170 updateCaptionRelativeView](#captions-stickers-170-updatecaptionrelativeview)
- [captions-stickers-171 generateKeyFrameInfo](#captions-stickers-171-generatekeyframeinfo)
- [captions-stickers-172 onClick](#captions-stickers-172-onclick)
- [captions-stickers-173 selectCaptionByZVal](#captions-stickers-173-selectcaptionbyzval)
- [captions-stickers-174 selectCaptionByZVal](#captions-stickers-174-selectcaptionbyzval)
- [captions-stickers-175 playVideo](#captions-stickers-175-playvideo)
- [captions-stickers-176 getCurCaptionZVal](#captions-stickers-176-getcurcaptionzval)
- [captions-stickers-177 addCaption](#captions-stickers-177-addcaption)
- [captions-stickers-178 addTimeSpan](#captions-stickers-178-addtimespan)
- [captions-stickers-179 rebuildBezierData](#captions-stickers-179-rebuildbezierdata)
- [captions-stickers-180 rebuildBezierData](#captions-stickers-180-rebuildbezierdata)
- [captions-stickers-181 addAllTimeSpan](#captions-stickers-181-addalltimespan)
- [captions-stickers-182 addAllTimeSpan](#captions-stickers-182-addalltimespan)
- [captions-stickers-183 selectCaption](#captions-stickers-183-selectcaption)
- [captions-stickers-184 selectCaption](#captions-stickers-184-selectcaption)
- [captions-stickers-185 selectTimeSpan](#captions-stickers-185-selecttimespan)
- [captions-stickers-186 selectTimeSpan](#captions-stickers-186-selecttimespan)
- [captions-stickers-187 playBackEOF](#captions-stickers-187-playbackeof)
- [captions-stickers-188 updateCaptionPosition](#captions-stickers-188-updatecaptionposition)
- [captions-stickers-189 updateCaptionPosition](#captions-stickers-189-updatecaptionposition)
- [captions-stickers-190 initCaptionStyleFragment](#captions-stickers-190-initcaptionstylefragment)
- [captions-stickers-191 initCaptionColorFragment](#captions-stickers-191-initcaptioncolorfragment)
- [captions-stickers-192 initCaptionOutlineFragment](#captions-stickers-192-initcaptionoutlinefragment)
- [captions-stickers-193 initCaptionBackgroundFragment](#captions-stickers-193-initcaptionbackgroundfragment)
- [captions-stickers-194 initCaptionLetterSpacingFragment](#captions-stickers-194-initcaptionletterspacingfragment)
- [captions-stickers-195 onSmallBtnClicked](#captions-stickers-195-onsmallbtnclicked)
- [captions-stickers-196 onSmallBtnClicked](#captions-stickers-196-onsmallbtnclicked)
- [captions-stickers-197 onStandardBtnClicked](#captions-stickers-197-onstandardbtnclicked)
- [captions-stickers-198 onStandardBtnClicked](#captions-stickers-198-onstandardbtnclicked)
- [captions-stickers-199 onMoreBtnClicked](#captions-stickers-199-onmorebtnclicked)
- [captions-stickers-200 onMoreBtnClicked](#captions-stickers-200-onmorebtnclicked)
- [captions-stickers-201 onLargeBtnClicked](#captions-stickers-201-onlargebtnclicked)
- [captions-stickers-202 onLargeBtnClicked](#captions-stickers-202-onlargebtnclicked)
- [captions-stickers-203 seekTimeline](#captions-stickers-203-seektimeline)
- [captions-stickers-204 initListener](#captions-stickers-204-initlistener)
- [captions-stickers-205 onSelectMode](#captions-stickers-205-onselectmode)
- [captions-stickers-206 onAdjustDataChanged](#captions-stickers-206-onadjustdatachanged)
- [captions-stickers-207 onAdjustDataChanged](#captions-stickers-207-onadjustdatachanged)
- [captions-stickers-208 onAdjustDataChanged](#captions-stickers-208-onadjustdatachanged)
- [captions-stickers-209 resetAdjustData](#captions-stickers-209-resetadjustdata)
- [captions-stickers-210 resetAdjustData](#captions-stickers-210-resetadjustdata)
- [captions-stickers-211 removeTimeline](#captions-stickers-211-removetimeline)
- [captions-stickers-212 initVideoFragment](#captions-stickers-212-initvideofragment)
- [captions-stickers-213 onClick](#captions-stickers-213-onclick)
- [captions-stickers-214 initVideoFragment](#captions-stickers-214-initvideofragment)
- [captions-stickers-215 initVideoFragment](#captions-stickers-215-initvideofragment)
- [captions-stickers-216 updateDurationSeekBar](#captions-stickers-216-updatedurationseekbar)
- [captions-stickers-217 initVideoFragment](#captions-stickers-217-initvideofragment)
- [captions-stickers-218 onClick](#captions-stickers-218-onclick)
- [captions-stickers-219 initVideoFragment](#captions-stickers-219-initvideofragment)
- [captions-stickers-220 initVideoFragment](#captions-stickers-220-initvideofragment)
- [captions-stickers-221 removeTimeline](#captions-stickers-221-removetimeline)
- [captions-stickers-222 initClipFragment](#captions-stickers-222-initclipfragment)
- [captions-stickers-223 seekTimeline](#captions-stickers-223-seektimeline)
- [captions-stickers-224 seekTimeline](#captions-stickers-224-seektimeline)
- [captions-stickers-225 SpiltTimeSpan](#captions-stickers-225-spilttimespan)
- [captions-stickers-226 initListener](#captions-stickers-226-initlistener)
- [captions-stickers-227 initListener](#captions-stickers-227-initlistener)
- [captions-stickers-228 onStopTrackingTouch](#captions-stickers-228-onstoptrackingtouch)
- [captions-stickers-229 onScrollX](#captions-stickers-229-onscrollx)
- [captions-stickers-230 onClick](#captions-stickers-230-onclick)
- [captions-stickers-231 initVideoFragment](#captions-stickers-231-initvideofragment)
- [captions-stickers-232 seekTimeline](#captions-stickers-232-seektimeline)
- [captions-stickers-233 initData](#captions-stickers-233-initdata)
- [captions-stickers-234 initCaptionStyleFragment](#captions-stickers-234-initcaptionstylefragment)
- [captions-stickers-235 onItemClick](#captions-stickers-235-onitemclick)
- [captions-stickers-236 onItemClick](#captions-stickers-236-onitemclick)
- [captions-stickers-237 initCaptionColorFragment](#captions-stickers-237-initcaptioncolorfragment)
- [captions-stickers-238 initCaptionOutlineFragment](#captions-stickers-238-initcaptionoutlinefragment)
- [captions-stickers-239 initCaptionBackgroundFragment](#captions-stickers-239-initcaptionbackgroundfragment)
- [captions-stickers-240 initCaptionBackgroundFragment](#captions-stickers-240-initcaptionbackgroundfragment)
- [captions-stickers-241 onCaptionColor](#captions-stickers-241-oncaptioncolor)
- [captions-stickers-242 setOnScrollListener](#captions-stickers-242-setonscrolllistener)
- [captions-stickers-243 onTouch](#captions-stickers-243-ontouch)
- [captions-stickers-244 playBackEOF](#captions-stickers-244-playbackeof)
- [captions-stickers-245 addCaption](#captions-stickers-245-addcaption)
- [captions-stickers-246 addAllTimeSpan](#captions-stickers-246-addalltimespan)
- [captions-stickers-247 initMultiSequence](#captions-stickers-247-initmultisequence)
- [captions-stickers-248 seekTimeline](#captions-stickers-248-seektimeline)
- [captions-stickers-249 createTimeline](#captions-stickers-249-createtimeline)
- [captions-stickers-250 applyMaskInfo](#captions-stickers-250-applymaskinfo)
- [captions-stickers-251 setVolumeGain](#captions-stickers-251-setvolumegain)
- [captions-stickers-252 streamingEngineStateChanged](#captions-stickers-252-streamingenginestatechanged)
- [captions-stickers-253 onAssetDelete](#captions-stickers-253-onassetdelete)
- [captions-stickers-254 onClick](#captions-stickers-254-onclick)
- [captions-stickers-255 onDestroy](#captions-stickers-255-ondestroy)
- [captions-stickers-256 isHasThemeCaptionTitle](#captions-stickers-256-ishasthemecaptiontitle)
- [captions-stickers-257 isHasThemeCaptionTitle](#captions-stickers-257-ishasthemecaptiontitle)
- [captions-stickers-258 isHasThemeCaptionTitle](#captions-stickers-258-ishasthemecaptiontitle)
- [captions-stickers-259 selectThemeCaption](#captions-stickers-259-selectthemecaption)
- [captions-stickers-260 selectThemeCaption](#captions-stickers-260-selectthemecaption)
- [captions-stickers-261 initTimelineEditor](#captions-stickers-261-inittimelineeditor)
- [captions-stickers-262 addTimeSpan](#captions-stickers-262-addtimespan)
- [captions-stickers-263 addDouVideoTimeSpan](#captions-stickers-263-adddouvideotimespan)
- [captions-stickers-264 addDouVideoTimeSpan](#captions-stickers-264-adddouvideotimespan)
- [captions-stickers-265 addTimeSpanExt](#captions-stickers-265-addtimespanext)
- [captions-stickers-266 selectTimeSpan](#captions-stickers-266-selecttimespan)
- [captions-stickers-267 timeSpanCount](#captions-stickers-267-timespancount)
- [captions-stickers-268 initVideoFragment](#captions-stickers-268-initvideofragment)
- [captions-stickers-269 initVideoFragment](#captions-stickers-269-initvideofragment)
- [captions-stickers-270 onBackPressed](#captions-stickers-270-onbackpressed)
- [captions-stickers-271 bindLayout](#captions-stickers-271-bindlayout)
- [captions-stickers-272 onTouch](#captions-stickers-272-ontouch)
- [captions-stickers-273 compileProgress](#captions-stickers-273-compileprogress)
- [captions-stickers-274 compileFinished](#captions-stickers-274-compilefinished)
- [captions-stickers-275 compileFailed](#captions-stickers-275-compilefailed)
- [captions-stickers-276 addCaption](#captions-stickers-276-addcaption)
- [captions-stickers-277 initListener](#captions-stickers-277-initlistener)
- [captions-stickers-278 initListener](#captions-stickers-278-initlistener)
- [captions-stickers-279 updateCompoundCaption](#captions-stickers-279-updatecompoundcaption)
- [captions-stickers-280 installAssetPackage](#captions-stickers-280-installassetpackage)
- [captions-stickers-281 installAssetPackage](#captions-stickers-281-installassetpackage)
- [captions-stickers-282 refreshCompoundCaptionView](#captions-stickers-282-refreshcompoundcaptionview)
- [captions-stickers-283 onActivityResult](#captions-stickers-283-onactivityresult)
- [captions-stickers-284 onActivityResult](#captions-stickers-284-onactivityresult)
- [captions-stickers-285 onActivityResult](#captions-stickers-285-onactivityresult)
- [captions-stickers-286 onActivityResult](#captions-stickers-286-onactivityresult)
- [captions-stickers-287 getType](#captions-stickers-287-gettype)
- [captions-stickers-288 getCompoundCaption](#captions-stickers-288-getcompoundcaption)
- [captions-stickers-289 addVideoClip](#captions-stickers-289-addvideoclip)
- [captions-stickers-290 addVideoClip](#captions-stickers-290-addvideoclip)
- [captions-stickers-291 applyClipAnimatedSticker](#captions-stickers-291-applyclipanimatedsticker)
- [captions-stickers-292 applyAnimatedStickerAnimation](#captions-stickers-292-applyanimatedstickeranimation)
- [captions-stickers-293 setCaption](#captions-stickers-293-setcaption)
- [captions-stickers-294 setCaption](#captions-stickers-294-setcaption)
- [captions-stickers-295 setCaption](#captions-stickers-295-setcaption)
- [captions-stickers-296 setCompoundCaption](#captions-stickers-296-setcompoundcaption)
- [captions-stickers-297 updateCaptionAttribute](#captions-stickers-297-updatecaptionattribute)
- [captions-stickers-298 applyMask](#captions-stickers-298-applymask)
- [captions-stickers-299 applyClipCaption](#captions-stickers-299-applyclipcaption)
- [captions-stickers-300 saveCaptionData](#captions-stickers-300-savecaptiondata)
- [captions-stickers-301 saveCaptionData](#captions-stickers-301-savecaptiondata)
- [captions-stickers-302 saveCompoundCaptionData](#captions-stickers-302-savecompoundcaptiondata)
- [captions-stickers-303 setCaptionBackgroundPadding](#captions-stickers-303-setcaptionbackgroundpadding)
- [captions-stickers-304 setList](#captions-stickers-304-setlist)
- [captions-stickers-305 initTimelineEditor](#captions-stickers-305-inittimelineeditor)
- [captions-stickers-306 addTimeSpan](#captions-stickers-306-addtimespan)
- [captions-stickers-307 addDouVideoTimeSpan](#captions-stickers-307-adddouvideotimespan)
- [captions-stickers-308 addDouVideoTimeSpan](#captions-stickers-308-adddouvideotimespan)
- [captions-stickers-309 addTimeSpanExt](#captions-stickers-309-addtimespanext)
- [captions-stickers-310 selectTimeSpan](#captions-stickers-310-selecttimespan)
- [captions-stickers-311 timeSpanCount](#captions-stickers-311-timespancount)
- [captions-stickers-312 moveAndRemoveNvsCaption](#captions-stickers-312-moveandremovenvscaption)
- [captions-stickers-313 moveAndRemoveNvsCaption](#captions-stickers-313-moveandremovenvscaption)
- [captions-stickers-314 moveAndRemoveNvsCaption](#captions-stickers-314-moveandremovenvscaption)
- [captions-stickers-315 moveAndRemoveNvsCaption](#captions-stickers-315-moveandremovenvscaption)
- [captions-stickers-316 addNvsCaption](#captions-stickers-316-addnvscaption)
- [captions-stickers-317 addNvsCaption](#captions-stickers-317-addnvscaption)
- [captions-stickers-318 addNvsCaption](#captions-stickers-318-addnvscaption)
- [captions-stickers-319 addNvsCaption](#captions-stickers-319-addnvscaption)
- [captions-stickers-320 changeAICaptionInPoint](#captions-stickers-320-changeaicaptioninpoint)
- [captions-stickers-321 changeAICaptionInPoint](#captions-stickers-321-changeaicaptioninpoint)
- [captions-stickers-322 changeAICaptionInPoint](#captions-stickers-322-changeaicaptioninpoint)
- [captions-stickers-323 changeAICaptionOutPoint](#captions-stickers-323-changeaicaptionoutpoint)
- [captions-stickers-324 changeAICaptionOutPoint](#captions-stickers-324-changeaicaptionoutpoint)
- [captions-stickers-325 changeAICaptionOutPoint](#captions-stickers-325-changeaicaptionoutpoint)
- [captions-stickers-326 addAnimatorSticker](#captions-stickers-326-addanimatorsticker)
- [captions-stickers-327 addCustomAnimatorSticker](#captions-stickers-327-addcustomanimatorsticker)
- [captions-stickers-328 setCompoundCaptionFont](#captions-stickers-328-setcompoundcaptionfont)
- [captions-stickers-329 setCompoundCaptionFont](#captions-stickers-329-setcompoundcaptionfont)
- [captions-stickers-330 seekTimeline](#captions-stickers-330-seektimeline)
- [captions-stickers-331 seekTimeline](#captions-stickers-331-seektimeline)
- [captions-stickers-332 addCaption](#captions-stickers-332-addcaption)
- [captions-stickers-333 updateCaption](#captions-stickers-333-updatecaption)
- [captions-stickers-334 removeCaption](#captions-stickers-334-removecaption)
- [captions-stickers-335 removeAllAICaption](#captions-stickers-335-removeallaicaption)
- [captions-stickers-336 removeAllAICaption](#captions-stickers-336-removeallaicaption)
- [captions-stickers-337 removeCaption](#captions-stickers-337-removecaption)
- [captions-stickers-338 handleCaptionColorConner](#captions-stickers-338-handlecaptioncolorconner)
- [captions-stickers-339 handleCaptionBackgroundColor](#captions-stickers-339-handlecaptionbackgroundcolor)
- [captions-stickers-340 handleCaptionOutlineWidth](#captions-stickers-340-handlecaptionoutlinewidth)
- [captions-stickers-341 handleCaptionOutLineColor](#captions-stickers-341-handlecaptionoutlinecolor)
- [captions-stickers-342 handleCaptionTextColor](#captions-stickers-342-handlecaptiontextcolor)
- [captions-stickers-343 handleCaptionFont](#captions-stickers-343-handlecaptionfont)
- [captions-stickers-344 handleCaptionShadow](#captions-stickers-344-handlecaptionshadow)
- [captions-stickers-345 handleCaptionItalics](#captions-stickers-345-handlecaptionitalics)
- [captions-stickers-346 handleCaptionBold](#captions-stickers-346-handlecaptionbold)
- [captions-stickers-347 setCaptionLetterSpace](#captions-stickers-347-setcaptionletterspace)
- [captions-stickers-348 setCaptionLineSpace](#captions-stickers-348-setcaptionlinespace)
- [captions-stickers-349 handleCaptionPosition](#captions-stickers-349-handlecaptionposition)
- [captions-stickers-350 handleCaptionAnimationCombination](#captions-stickers-350-handlecaptionanimationcombination)
- [captions-stickers-351 handleCaptionAnimationOut](#captions-stickers-351-handlecaptionanimationout)
- [captions-stickers-352 handleCaptionAnimationIn](#captions-stickers-352-handlecaptionanimationin)
- [captions-stickers-353 deleteSticker](#captions-stickers-353-deletesticker)
- [captions-stickers-354 removeCompoundCaption](#captions-stickers-354-removecompoundcaption)
- [captions-stickers-355 copyCaption](#captions-stickers-355-copycaption)
- [captions-stickers-356 changeStickerVoice](#captions-stickers-356-changestickervoice)
- [captions-stickers-357 changeStickerMirror](#captions-stickers-357-changestickermirror)
- [captions-stickers-358 applyCaptionPositionToAll](#captions-stickers-358-applycaptionpositiontoall)
- [captions-stickers-359 applyCaptionFontToAll](#captions-stickers-359-applycaptionfonttoall)
- [captions-stickers-360 applyCaptionLetterSpaceToAll](#captions-stickers-360-applycaptionletterspacetoall)
- [captions-stickers-361 applyCaptionOutlineToAll](#captions-stickers-361-applycaptionoutlinetoall)
- [captions-stickers-362 removeCaptionOutlineColor](#captions-stickers-362-removecaptionoutlinecolor)
- [captions-stickers-363 removeCaptionBackgroundColor](#captions-stickers-363-removecaptionbackgroundcolor)
- [captions-stickers-364 removeCaptionBackgroundColor](#captions-stickers-364-removecaptionbackgroundcolor)
- [captions-stickers-365 setCaptionBackgroundColor](#captions-stickers-365-setcaptionbackgroundcolor)
- [captions-stickers-366 setCaptionOutLineColor](#captions-stickers-366-setcaptionoutlinecolor)
- [captions-stickers-367 setCaptionTextColor](#captions-stickers-367-setcaptiontextcolor)
- [captions-stickers-368 updateCaptionTranslation](#captions-stickers-368-updatecaptiontranslation)
- [captions-stickers-369 updateCaptionTranslation](#captions-stickers-369-updatecaptiontranslation)
- [captions-stickers-370 updateStickerTranslation](#captions-stickers-370-updatestickertranslation)
- [captions-stickers-371 updateStickerTranslation](#captions-stickers-371-updatestickertranslation)
- [captions-stickers-372 updateCompoundCaptionTranslation](#captions-stickers-372-updatecompoundcaptiontranslation)
- [captions-stickers-373 updateCompoundCaptionTranslation](#captions-stickers-373-updatecompoundcaptiontranslation)
- [captions-stickers-374 updateCaptionScale](#captions-stickers-374-updatecaptionscale)
- [captions-stickers-375 updateCaptionScale](#captions-stickers-375-updatecaptionscale)
- [captions-stickers-376 updateStickerScale](#captions-stickers-376-updatestickerscale)
- [captions-stickers-377 updateStickerScale](#captions-stickers-377-updatestickerscale)
- [captions-stickers-378 updateCompoundCaptionScale](#captions-stickers-378-updatecompoundcaptionscale)
- [captions-stickers-379 updateCompoundCaptionScale](#captions-stickers-379-updatecompoundcaptionscale)
- [captions-stickers-380 getTranslationX](#captions-stickers-380-gettranslationx)
- [captions-stickers-381 getTranslationY](#captions-stickers-381-gettranslationy)
- [captions-stickers-382 getFont](#captions-stickers-382-getfont)
- [captions-stickers-383 getLineSpacing](#captions-stickers-383-getlinespacing)
- [captions-stickers-384 getTextColor](#captions-stickers-384-gettextcolor)
- [captions-stickers-385 isBold](#captions-stickers-385-isbold)
- [captions-stickers-386 isItalic](#captions-stickers-386-isitalic)
- [captions-stickers-387 isShadow](#captions-stickers-387-isshadow)
- [captions-stickers-388 isOutline](#captions-stickers-388-isoutline)
- [captions-stickers-389 getOutlineColor](#captions-stickers-389-getoutlinecolor)
- [captions-stickers-390 getLetterSpacing](#captions-stickers-390-getletterspacing)
- [captions-stickers-391 getBackgroundColor](#captions-stickers-391-getbackgroundcolor)
- [captions-stickers-392 getBackgroundAngle](#captions-stickers-392-getbackgroundangle)
- [captions-stickers-393 getRichWordUuid](#captions-stickers-393-getrichworduuid)
- [captions-stickers-394 getBubbleUuid](#captions-stickers-394-getbubbleuuid)
- [captions-stickers-395 setOperationType](#captions-stickers-395-setoperationtype)
- [captions-stickers-396 bindToTimeline](#captions-stickers-396-bindtotimeline)
- [captions-stickers-397 loadData](#captions-stickers-397-loaddata)
- [captions-stickers-398 setItemSelectedIndex](#captions-stickers-398-setitemselectedindex)
- [captions-stickers-399 addCompoundCaptionFirst](#captions-stickers-399-addcompoundcaptionfirst)
- [captions-stickers-400 getCustomanimatedStickerImagePath](#captions-stickers-400-getcustomanimatedstickerimagepath)
- [captions-stickers-401 setzValue](#captions-stickers-401-setzvalue)
- [captions-stickers-402 LogStickerAndCaption](#captions-stickers-402-logstickerandcaption)
- [captions-stickers-403 LogStickerAndCaption](#captions-stickers-403-logstickerandcaption)
- [captions-stickers-404 LogStickerAndCaption](#captions-stickers-404-logstickerandcaption)
- [captions-stickers-405 getCaptionByAttachment](#captions-stickers-405-getcaptionbyattachment)
- [captions-stickers-406 setItemSelectedIndex](#captions-stickers-406-setitemselectedindex)
- [captions-stickers-407 setSitckerCaptionObject](#captions-stickers-407-setsitckercaptionobject)
- [captions-stickers-408 removeAllSticker](#captions-stickers-408-removeallsticker)
<!-- END GENERATED CONTENTS -->

## `captions-stickers-001` `onScaleAndRotate`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:570`

API classes: `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`
Common calls: `mapViewToCanonical()`, `getAttachment()`, `scaleAnimatedSticker()`, `rotateAnimatedSticker()`, `getHorizontalFlip()`, `getBoundingRectangleVertices()`, `scaleCaption()`, `rotateCaption()`, `getCompoundBoundingVertices()`

Simple sequence:

```java
if (mLiveWindow instanceof MSLiveWindow) {
assetAnchor = ((MSLiveWindow) mLiveWindow).mapViewToCanonical(anchor);
} else if (mLiveWindow instanceof MSLiveWindowExt) {
assetAnchor = ((MSLiveWindowExt) mLiveWindow).mapViewToCanonical(anchor);
updateDrawRectPosition(getAssetViewVerticesList(currentAnimatedSticker.getHorizontalFlip(), currentAnimatedSticker.getBoundingRectangleVertices())
, Constants.EDIT_MODE_STICKER, (String) currentAnimatedSticker.getAttachment(Constants.KEY_LEVEL), null);
false, currentCompoundCaption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME));
(String) currentCompoundCaption.getAttachment(Constants.KEY_LEVEL), captions);
```

## `captions-stickers-002` `deleteCaptionOrSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:819`

API classes: `NvsCaptureAnimatedSticker`, `NvsCaptureCompoundCaption`
Common calls: `getAttachment()`, `equals()`, `getTag()`, `isEmpty()`, `remove()`, `setVisibility()`, `get()`, `getCaptureAnimatedStickerCount()`, `getCaptureAnimatedStickerByIndex()`, `removeCaptureAnimatedSticker()`, `getCaptureCompoundCaptionCount()`, `getCaptureCompoundCaptionByIndex()`

Simple sequence:

```java
if (currentAnimatedSticker != null) {
String kValue = (String) currentAnimatedSticker.getAttachment(Constants.KEY_LEVEL);
int count = mStreamingContext.getCaptureAnimatedStickerCount();
for (int i = 0; i < count; i++) {
NvsCaptureAnimatedSticker animatedSticker = mStreamingContext.getCaptureAnimatedStickerByIndex(i);
if (!TextUtils.isEmpty(kValue) && animatedSticker != null
&& TextUtils.equals(kValue, (String) animatedSticker.getAttachment(Constants.KEY_LEVEL))) {
for (AssetLevelBean captionVertex : stickerVertices) {
if (TextUtils.equals(kValue, captionVertex.getTag())) {
mStreamingContext.removeCaptureAnimatedSticker(i);
drawRect.setVisibility(View.GONE);
if (!stickerVertices.isEmpty()) {
checkSelectByAttachment(stickerVertices.get(0).getTag());
if (currentCompoundCaption != null) {
String kValue = (String) currentCompoundCaption.getAttachment(Constants.KEY_LEVEL);
int count = mStreamingContext.getCaptureCompoundCaptionCount();
for (int i = 0; i < count; i++) {
NvsCaptureCompoundCaption compoundCaption = mStreamingContext.getCaptureCompoundCaptionByIndex(i);
if (!TextUtils.isEmpty(kValue) && compoundCaption != null
&& TextUtils.equals(kValue, (String) compoundCaption.getAttachment(Constants.KEY_LEVEL))) {
for (AssetLevelBean captionVertex : captionVertices) {
if (TextUtils.equals(kValue, captionVertex.getTag())) {
mStreamingContext.removeCaptureCompoundCaption(i);
drawRect.setVisibility(View.GONE);
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-003` `deleteCaptionOrSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:820`

API classes: `NvsCaptureAnimatedSticker`, `NvsCaptureCompoundCaption`
Common calls: `getAttachment()`, `equals()`, `getTag()`, `isEmpty()`, `remove()`, `setVisibility()`, `get()`, `getCaptureAnimatedStickerCount()`, `getCaptureAnimatedStickerByIndex()`, `removeCaptureAnimatedSticker()`, `getCaptureCompoundCaptionCount()`, `getCaptureCompoundCaptionByIndex()`

Simple sequence:

```java
if (currentAnimatedSticker != null) {
String kValue = (String) currentAnimatedSticker.getAttachment(Constants.KEY_LEVEL);
int count = mStreamingContext.getCaptureAnimatedStickerCount();
for (int i = 0; i < count; i++) {
NvsCaptureAnimatedSticker animatedSticker = mStreamingContext.getCaptureAnimatedStickerByIndex(i);
if (!TextUtils.isEmpty(kValue) && animatedSticker != null
&& TextUtils.equals(kValue, (String) animatedSticker.getAttachment(Constants.KEY_LEVEL))) {
for (AssetLevelBean captionVertex : stickerVertices) {
if (TextUtils.equals(kValue, captionVertex.getTag())) {
mStreamingContext.removeCaptureAnimatedSticker(i);
drawRect.setVisibility(View.GONE);
if (!stickerVertices.isEmpty()) {
checkSelectByAttachment(stickerVertices.get(0).getTag());
if (currentCompoundCaption != null) {
String kValue = (String) currentCompoundCaption.getAttachment(Constants.KEY_LEVEL);
int count = mStreamingContext.getCaptureCompoundCaptionCount();
for (int i = 0; i < count; i++) {
NvsCaptureCompoundCaption compoundCaption = mStreamingContext.getCaptureCompoundCaptionByIndex(i);
if (!TextUtils.isEmpty(kValue) && compoundCaption != null
&& TextUtils.equals(kValue, (String) compoundCaption.getAttachment(Constants.KEY_LEVEL))) {
for (AssetLevelBean captionVertex : captionVertices) {
if (TextUtils.equals(kValue, captionVertex.getTag())) {
mStreamingContext.removeCaptureCompoundCaption(i);
drawRect.setVisibility(View.GONE);
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-004` `deleteCaptionOrSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:821`

API classes: `NvsCaptureAnimatedSticker`
Common calls: `getAttachment()`, `isEmpty()`, `equals()`, `getTag()`, `getCaptureAnimatedStickerCount()`, `getCaptureAnimatedStickerByIndex()`, `remove()`, `removeCaptureAnimatedSticker()`, `setVisibility()`, `get()`

Simple sequence:

```java
if (currentAnimatedSticker != null) {
String kValue = (String) currentAnimatedSticker.getAttachment(Constants.KEY_LEVEL);
int count = mStreamingContext.getCaptureAnimatedStickerCount();
for (int i = 0; i < count; i++) {
NvsCaptureAnimatedSticker animatedSticker = mStreamingContext.getCaptureAnimatedStickerByIndex(i);
if (!TextUtils.isEmpty(kValue) && animatedSticker != null
&& TextUtils.equals(kValue, (String) animatedSticker.getAttachment(Constants.KEY_LEVEL))) {
for (AssetLevelBean captionVertex : stickerVertices) {
if (TextUtils.equals(kValue, captionVertex.getTag())) {
mStreamingContext.removeCaptureAnimatedSticker(i);
drawRect.setVisibility(View.GONE);
if (!stickerVertices.isEmpty()) {
checkSelectByAttachment(stickerVertices.get(0).getTag());
```

## `captions-stickers-005` `deleteCaptionOrSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:824`

API classes: `NvsCaptureAnimatedSticker`
Common calls: `equals()`, `getCaptureAnimatedStickerByIndex()`, `isEmpty()`, `getAttachment()`, `getTag()`, `remove()`, `removeCaptureAnimatedSticker()`, `setVisibility()`

Simple sequence:

```java
for (int i = 0; i < count; i++) {
NvsCaptureAnimatedSticker animatedSticker = mStreamingContext.getCaptureAnimatedStickerByIndex(i);
if (!TextUtils.isEmpty(kValue) && animatedSticker != null
&& TextUtils.equals(kValue, (String) animatedSticker.getAttachment(Constants.KEY_LEVEL))) {
for (AssetLevelBean captionVertex : stickerVertices) {
if (TextUtils.equals(kValue, captionVertex.getTag())) {
mStreamingContext.removeCaptureAnimatedSticker(i);
drawRect.setVisibility(View.GONE);
```

## `captions-stickers-006` `checkSelectCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:917`

API classes: `NvsCaption`
Static/constants: `NvsCaption.BOUNDING_TYPE_TEXT`
Common calls: `isEmpty()`, `getAttachment()`, `equals()`, `getCaptionCount()`, `getCaptionBoundingVertices()`

Simple sequence:

```java
if (currentCompoundCaption != null) {
oldKey = (String) currentCompoundCaption.getAttachment(Constants.KEY_LEVEL);
if (currentCompoundCaption != null) {
int captionCount = currentCompoundCaption.getCaptionCount();
for (int i = 0; i < captionCount; i++) {
List<PointF> captionBoundingVertices = currentCompoundCaption.getCaptionBoundingVertices(i, NvsCaption.BOUNDING_TYPE_TEXT);
```

## `captions-stickers-007` `getCaptionList`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1185`

API classes: `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT`
Common calls: `getCaptionCount()`, `getCaptionBoundingVertices()`, `add()`

Simple sequence:

```java
if (compoundCaption != null) {
int captionCount = compoundCaption.getCaptionCount();
for (int i = 0; i < captionCount; i++) {
List<PointF> pointFS = compoundCaption.getCaptionBoundingVertices(i, NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT);
```

## `captions-stickers-008` `getCaptionList`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1187`

API classes: `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT`
Common calls: `getCaptionBoundingVertices()`, `add()`

Simple sequence:

```java
for (int i = 0; i < captionCount; i++) {
List<PointF> pointFS = compoundCaption.getCaptionBoundingVertices(i, NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT);
```

## `captions-stickers-009` `checkSelectByAttachment`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1851`

API classes: `NvsCaptureAnimatedSticker`, `NvsCaptureCompoundCaption`, `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`
Common calls: `equals()`, `get()`, `getAttachment()`, `size()`, `getTag()`, `remove()`, `add()`, `isEmpty()`, `findFragmentByTag()`, `getCaptureAnimatedStickerCount()`, `getCaptureAnimatedStickerByIndex()`, `selectEffectById()`

Simple sequence:

```java
int count = mStreamingContext.getCaptureAnimatedStickerCount();
for (int i = 0; i < count; i++) {
NvsCaptureAnimatedSticker animatedSticker = mStreamingContext.getCaptureAnimatedStickerByIndex(i);
if (animatedSticker != null && TextUtils.equals(attachment, (String) animatedSticker.getAttachment(Constants.KEY_LEVEL))) {
captureEffectFragment.selectEffectById(currentAnimatedSticker.getAnimatedStickerPackageId());
updateDrawRectPosition(getAssetViewVerticesList(currentAnimatedSticker.getHorizontalFlip(), currentAnimatedSticker.getBoundingRectangleVertices()), drawRectModel, attachment, null);
for (int j = 0; j < stickerVertices.size(); j++) {
if (TextUtils.equals(stickerVertices.get(j).getTag(), attachment)) {
int count = mStreamingContext.getCaptureCompoundCaptionCount();
for (int i = 0; i < count; i++) {
NvsCaptureCompoundCaption compoundCaption = mStreamingContext.getCaptureCompoundCaptionByIndex(i);
if (compoundCaption != null && TextUtils.equals(attachment, (String) compoundCaption.getAttachment(Constants.KEY_LEVEL))) {
List<PointF> vertices = currentCompoundCaption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);
for (int j = 0; j < captionVertices.size(); j++) {
if (TextUtils.equals(captionVertices.get(j).getTag(), attachment)) {
```

## `captions-stickers-010` `checkSelectByAttachment`

Source: `app/src/main/java/com/meishe/sdkdemo/capture/CaptureActivity.java:1855`

API classes: `NvsCaptureAnimatedSticker`, `NvsCaptureCompoundCaption`, `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`
Common calls: `equals()`, `get()`, `getAttachment()`, `size()`, `getTag()`, `remove()`, `add()`, `findFragmentByTag()`, `getCaptureAnimatedStickerCount()`, `getCaptureAnimatedStickerByIndex()`, `selectEffectById()`, `getAnimatedStickerPackageId()`

Simple sequence:

```java
int count = mStreamingContext.getCaptureAnimatedStickerCount();
for (int i = 0; i < count; i++) {
NvsCaptureAnimatedSticker animatedSticker = mStreamingContext.getCaptureAnimatedStickerByIndex(i);
if (animatedSticker != null && TextUtils.equals(attachment, (String) animatedSticker.getAttachment(Constants.KEY_LEVEL))) {
captureEffectFragment.selectEffectById(currentAnimatedSticker.getAnimatedStickerPackageId());
updateDrawRectPosition(getAssetViewVerticesList(currentAnimatedSticker.getHorizontalFlip(), currentAnimatedSticker.getBoundingRectangleVertices()), drawRectModel, attachment, null);
for (int j = 0; j < stickerVertices.size(); j++) {
if (TextUtils.equals(stickerVertices.get(j).getTag(), attachment)) {
int count = mStreamingContext.getCaptureCompoundCaptionCount();
for (int i = 0; i < count; i++) {
NvsCaptureCompoundCaption compoundCaption = mStreamingContext.getCaptureCompoundCaptionByIndex(i);
if (compoundCaption != null && TextUtils.equals(attachment, (String) compoundCaption.getAttachment(Constants.KEY_LEVEL))) {
List<PointF> vertices = currentCompoundCaption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);
for (int j = 0; j < captionVertices.size(); j++) {
if (TextUtils.equals(captionVertices.get(j).getTag(), attachment)) {
```

## `captions-stickers-011` `initData`

Source: `app/src/main/java/com/meishe/sdkdemo/dialog/CaptionEditPop.java:155`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setAsset()`, `setAssetMode()`, `add()`, `getInstance()`, `readAssetJsonFile()`, `isEmpty()`, `fromJson()`, `getType()`, `size()`, `get()`, `getFontFileName()`, `registerFontByFilePath()`

Simple sequence:

```java
assetItem.setImageRes(R.mipmap.comp_caption_default);
assetItem.setAssetMode(AssetItem.ASSET_NONE);
assetItem.setAsset(asset);
captionFont.setLayoutManager(new LinearLayoutManager(getContext(), LinearLayoutManager.HORIZONTAL, false));
captionFont.setAdapter(fontAdapter);
```

## `captions-stickers-012` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoEditActivity.java:992`

API classes: `NvsStreamingContext`, `NvsTimeline`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `seekTimeline()`, `getDuration()`, `setFirstValue()`

Simple sequence:

```java
private void seekTimeline(NvsTimeline timeline, long timestamp) {
if (timeline == null)
mStreamingContext.seekTimeline(timeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER | NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
long duration = timeline.getDuration();
mFxSeekView.setFirstValue(mProgress);
```

## `captions-stickers-013` `OnRightTextClick`

Source: `app/src/main/java/com/meishe/sdkdemo/douvideo/DouVideoTrimActivity.java:163`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnTrimInChangeListener`, `NvsTimelineTimeSpan.OnTrimOutChangeListener`
Common calls: `setOnChangeListener()`, `OnTrimInChangeListener()`, `setVideoTrimIn()`, `OnTrimOutChangeListener()`, `setVideoTrimOut()`

Simple sequence:

```java
if (mDouVideoTimeSpan != null) {
mDouVideoTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {
mClipFragment.setVideoTrimIn(timeStamp);
mDouVideoTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimOutChangeListener() {
mClipFragment.setVideoTrimOut(timeStamp);
```

## `captions-stickers-014` `playbackTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:173`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER | flag);
```

## `captions-stickers-015` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:176`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-016` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:225`

API classes: `NvsTimelineEditor`
Common calls: `setMax()`, `setText()`, `valueOf()`, `getMultiThumbnailSequenceView()`

Simple sequence:

```java
mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.caption_timeline_editor);
alphaSeek.setMax(100);
seekBarOpacityWidthValue.setText(String.valueOf(100));
mMultiSequenceView = mTimelineEditor.getMultiThumbnailSequenceView();
```

## `captions-stickers-017` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:345`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOpacity()`, `getTimelineCurrentPosition()`, `getMax()`, `setText()`, `valueOf()`, `getInPoint()`, `setFloatValAtTime()`, `getStreamingEngineState()`

Simple sequence:

```java
if (mCurCaption != null) {
float opacity = i * 1f / alphaSeek.getMax();
seekBarOpacityWidthValue.setText(String.valueOf(i));
if (currentCaptionInfo != null) {
currentCaptionInfo.setOpacity(opacity);
mCurCaption.setOpacity(opacity);
long duration = mStreamingContext.getTimelineCurrentPosition(mTimeline) - mCurCaption.getInPoint();
mCurCaption.setFloatValAtTime(TRACK_OPACITY, opacity, duration);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-018` `onProgressChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:349`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOpacity()`, `getTimelineCurrentPosition()`, `getMax()`, `setText()`, `valueOf()`, `getInPoint()`, `setFloatValAtTime()`, `getStreamingEngineState()`

Simple sequence:

```java
if (mCurCaption != null) {
float opacity = i * 1f / alphaSeek.getMax();
seekBarOpacityWidthValue.setText(String.valueOf(i));
if (currentCaptionInfo != null) {
currentCaptionInfo.setOpacity(opacity);
mCurCaption.setOpacity(opacity);
long duration = mStreamingContext.getTimelineCurrentPosition(mTimeline) - mCurCaption.getInPoint();
mCurCaption.setFloatValAtTime(TRACK_OPACITY, opacity, duration);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-019` `onScrollX`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:393`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getTimelineCurrentPosition()`, `getAction()`, `setDrawRectVisible()`, `unSelectAllTimeSpan()`, `setTimelineScaleForSeek()`, `getDurationWidth()`, `getInstance()`, `getVisibility()`

Simple sequence:

```java
switch (event.getAction()) {
mVideoFragment.setDrawRectVisible(View.GONE);
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));
if (mLlKeyFrame.getVisibility() == View.VISIBLE) {
updateCaptionRelativeView(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-020` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:424`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-021` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:429`

API classes: `NvsTimeline`
Common calls: `setDrawRectVisible()`, `unSelectAllTimeSpan()`, `round()`, `getDuration()`, `getSequenceWidth()`, `smoothScrollTo()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
mVideoFragment.setDrawRectVisible(View.GONE);
if (mMultiSequenceView != null) {
int x = Math.round((stamp / (float) mTimeline.getDuration() * mTimelineEditor.getSequenceWidth()));
```

## `captions-stickers-022` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:442`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `getKeyFrameInfo()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_play);
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
updateKeyFrameView(mStreamingContext.getTimelineCurrentPosition(mTimeline), keyFrameInfo);
```

## `captions-stickers-023` `updateCaptionControlPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:800`

API classes: `NvsPointD`, `NvsControlPointPair`
Common calls: `getInPoint()`, `getValue()`, `getControlPoint()`, `setControlPoint()`, `getTranslation()`, `setCurrentKeyFrameTime()`, `setForwardControlPointX()`, `setForwardControlPointYForTransX()`, `setForwardControlPointYForTransY()`, `setBackwardControlPointX()`, `setBackwardControlPointYForTransX()`, `setBackwardControlPointYForTransY()`

Simple sequence:

```java
PointF beforePointF = mBeforeKeyMapInfo.getValue().getTranslation();
PointF nextPointF = mNextKeyMapInfo.getValue().getTranslation();
mCurCaption.setCurrentKeyFrameTime(beforeTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (pairY == null) {
pairY = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairY.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransY);
mCurCaption.setControlPoint(TRANS_Y, pairY);
KeyFrameInfo keyFrameInfo = mBeforeKeyMapInfo.getValue();
keyFrameInfo.setForwardControlPointX(forwardControlPointX);
keyFrameInfo.setForwardControlPointYForTransX(forwardControlPointYForTransX);
keyFrameInfo.setForwardControlPointYForTransY(forwardControlPointYForTransY);
mCurCaption.setCurrentKeyFrameTime(nextTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.backwardControlPoint = new NvsPointD(backwardControlPointX - mCurCaption.getInPoint(), backwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
// ... 8 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-024` `updateCaptionControlPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:803`

API classes: `NvsPointD`, `NvsControlPointPair`
Common calls: `getInPoint()`, `getControlPoint()`, `setControlPoint()`, `setCurrentKeyFrameTime()`, `getValue()`, `setForwardControlPointX()`, `setForwardControlPointYForTransX()`, `setForwardControlPointYForTransY()`, `setBackwardControlPointX()`, `setBackwardControlPointYForTransX()`, `setBackwardControlPointYForTransY()`

Simple sequence:

```java
mCurCaption.setCurrentKeyFrameTime(beforeTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (pairY == null) {
pairY = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairY.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransY);
mCurCaption.setControlPoint(TRANS_Y, pairY);
KeyFrameInfo keyFrameInfo = mBeforeKeyMapInfo.getValue();
keyFrameInfo.setForwardControlPointX(forwardControlPointX);
keyFrameInfo.setForwardControlPointYForTransX(forwardControlPointYForTransX);
keyFrameInfo.setForwardControlPointYForTransY(forwardControlPointYForTransY);
mCurCaption.setCurrentKeyFrameTime(nextTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.backwardControlPoint = new NvsPointD(backwardControlPointX - mCurCaption.getInPoint(), backwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (pairY == null) {
pairY = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
// ... 6 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-025` `updateCaptionRelativeView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:855`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`
Common calls: `getInPoint()`, `getKey()`, `getMax()`, `getZValue()`, `getKeyFrameInfo()`, `getTimelineCurrentPosition()`, `getFloatValAtTime()`, `setProgress()`, `setText()`, `valueOf()`, `getOutPoint()`, `setDrawRectVisible()`

Simple sequence:

```java
if (mCurCaption != null) {
captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
keyFrameMap = captionInfo.getKeyFrameInfo();
long currentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
&& (currentPosition - mCurCaption.getInPoint() >= minTime)
&& (currentPosition - mCurCaption.getInPoint() <= maxTime)) {
double floatValAtTime = mCurCaption.getFloatValAtTime(TRACK_OPACITY, currentPosition - mCurCaption.getInPoint());
alphaSeek.setProgress((int) ((floatValAtTime) * alphaSeek.getMax()));
seekBarOpacityWidthValue.setText(String.valueOf((int) ((floatValAtTime) * alphaSeek.getMax())));
if (mCurCaption != null) {
if (timeStamp > mCurCaption.getOutPoint() + 1000 || timeStamp < mCurCaption.getInPoint() - 1000) {
mVideoFragment.setDrawRectVisible(View.GONE);
for (Map.Entry<Long, KeyFrameInfo> entry : keyFrameMap.entrySet()) {
if (timeStamp >= entry.getKey() - 100000 && timeStamp <= entry.getKey() + 100000) {
currentKeyFrameStamp = entry.getKey();
if (hasKeyFrame) {
mCurCaption.setCurrentKeyFrameTime(currentKeyFrameStamp - mCurCaption.getInPoint());
mTvAddDeleteFrame.setEnabled(true);
if (mTimeline != null) {
seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `captions-stickers-026` `generateKeyFrameInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1142`

API classes: `NvsTimelineCaption`
Common calls: `setScaleX()`, `getScaleX()`, `setScaleY()`, `getScaleY()`, `setRotationZ()`, `getRotationZ()`, `setTranslation()`, `getCaptionTranslation()`, `setOpacity()`, `getOpacity()`

Simple sequence:

```java
private KeyFrameInfo generateKeyFrameInfo(NvsTimelineCaption caption) {
return new KeyFrameInfo().setScaleX(caption.getScaleX())
.setScaleY(caption.getScaleY())
.setRotationZ(caption.getRotationZ())
.setTranslation(caption.getCaptionTranslation()).setOpacity(caption.getOpacity());
```

## `captions-stickers-027` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1152`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getInstance()`, `instance()`, `putBoolean()`, `setVisibility()`, `getTimelineCurrentPosition()`, `setCurrentTime()`, `jumpActivityForResult()`, `currentActivity()`, `setCaptionData()`, `OnCloseListener()`, `getUserInputText()`, `show()`

Simple sequence:

```java
mCaptionStyleButton.setClickable(false);
if (currentCaptionInfo1 != null) {
currentCaptionInfo1.setTranslation(mCurCaption.getCaptionTranslation());
currentCaptionInfo1.setScaleFactorX(mCurCaption.getScaleX());
currentCaptionInfo1.setScaleFactorY(mCurCaption.getScaleY());
currentCaptionInfo1.setRotation(mCurCaption.getRotationZ());
BackupData.instance().setCaptionData(mCaptionDataListClone);
if (null != mCurCaption) {
BackupData.instance().setCaptionZVal((int) mCurCaption.getZValue());
BackupData.instance().setCurrentTime(mStreamingContext.getTimelineCurrentPosition(mTimeline));
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), CaptionStyleActivity.class, bundle, REQUESTCAPTIONSTYLE);
BackupData.instance().setCurrentTime(mStreamingContext.getTimelineCurrentPosition(mTimeline));
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), CaptionStyleActivity.class, bundle, REQUESTCAPTIONSTYLE);
BackupData.instance().setCurrentTime(mStreamingContext.getTimelineCurrentPosition(mTimeline));
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), CaptionStyleActivity.class, bundle, REQUESTCAPTIONSTYLE);
if (mLlKeyFrame.getVisibility() == View.VISIBLE) {
Map<Long, KeyFrameInfo> keyFrameInfo = currentCaptionInfo.getKeyFrameInfo();
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
mCaptionStyleButton.setVisibility(View.VISIBLE);
mStreamingContext.stop();
TimelineData.instance().setCaptionData(mCaptionDataListClone);
AppManager.getInstance().finishActivity();
if (mAddKeyFrame) {
// ... 14 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-028` `selectCaptionByZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1645`

API classes: `NvsTimelineCaption`
Common calls: `get()`, `getZValue()`, `setVisibility()`, `getTimelineCurrentPosition()`, `getCaptionsByTimelinePosition()`, `size()`, `getKeyFrameInfo()`, `isEmpty()`

Simple sequence:

```java
if (mTimeline != null) {
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineCaption> captionList = mTimeline.getCaptionsByTimelinePosition(curPos);
for (int i = 0; i < captionCount; i++) {
int zVal = (int) captionList.get(i).getZValue();
if (mCurCaption != null) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
mCaptionStyleButton.setVisibility(View.GONE);
```

## `captions-stickers-029` `selectCaptionByZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1646`

API classes: `NvsTimelineCaption`
Common calls: `get()`, `getZValue()`, `setVisibility()`, `getTimelineCurrentPosition()`, `getCaptionsByTimelinePosition()`, `size()`, `getKeyFrameInfo()`, `isEmpty()`

Simple sequence:

```java
if (mTimeline != null) {
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineCaption> captionList = mTimeline.getCaptionsByTimelinePosition(curPos);
for (int i = 0; i < captionCount; i++) {
int zVal = (int) captionList.get(i).getZValue();
if (mCurCaption != null) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
mCaptionStyleButton.setVisibility(View.GONE);
```

## `captions-stickers-030` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1675`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getTimelineCurrentPosition()`, `getDuration()`, `playVideo()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
```

## `captions-stickers-031` `getCurCaptionZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1702`

API classes: `NvsTimelineCaption`
Common calls: `getFirstCaption()`, `getZValue()`, `getNextCaption()`

Simple sequence:

```java
NvsTimelineCaption caption = mTimeline.getFirstCaption();
while (caption != null) {
float tmpZVal = caption.getZValue();
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-032` `addCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1803`

API classes: `NvsTimelineTimeSpan`
Common calls: `e()`, `add()`, `getOpacity()`, `getMax()`, `getTimelineCurrentPosition()`, `getDuration()`, `addCaption()`, `addModularCaption()`, `setZValue()`, `setVisibility()`, `setTraditional()`, `getTimeSpanshadowView()`

Simple sequence:

```java
long inPoint = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long duration = mTimeline.getDuration();
if (traditional) {
mCurCaption = mTimeline.addCaption(caption, inPoint, captionDuration, null);
mCurCaption = mTimeline.addModularCaption(caption, inPoint, captionDuration);
mCurCaption.setZValue(zVal);
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
mCaptionStyleButton.setVisibility(View.VISIBLE);
info.setTraditional(traditional);
timeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
mVideoFragment.setCurCaption(mCurCaption);
int alignVal = mCurCaption.getTextAlignment();
mVideoFragment.setAlignIndex(alignVal);
mVideoFragment.changeCaptionRectVisible();
if (captionInfo != null) {
captionInfo.setTraditionCaption(traditional);
if (mCurCaption != null) {
alphaSeek.setProgress((int) (mCurCaption.getOpacity() * alphaSeek.getMax()));
seekBarOpacityWidthValue.setText(String.valueOf((int) (mCurCaption.getOpacity() * alphaSeek.getMax())));
```

## `captions-stickers-033` `addTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:1874`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnTrimInChangeListener`, `NvsTimelineTimeSpan.OnTrimOutChangeListener`
Common calls: `getKey()`, `getKeyFrameInfo()`, `entrySet()`, `getTimelineCurrentPosition()`, `getInPoint()`, `setOnChangeListener()`, `changeCaptionRectVisible()`, `getZValue()`, `get()`, `isEmpty()`, `iterator()`, `hasNext()`

Simple sequence:

```java
private NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");
NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);
timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {
mVideoFragment.changeCaptionRectVisible();
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentCaptionInfo != null && mAddKeyFrame) {
currentTimeSpan.setKeyFrameInfo(currentCaptionInfo.getKeyFrameInfo());
if (mCurCaption != null) {
mCurCaption.changeInPoint(timeStamp);
int zVal = (int) mCurCaption.getZValue();
if (index >= 0) {
mCaptionDataListClone.get(index).setInPoint(timeStamp);
mVideoFragment.setDrawRectVisible(View.GONE);
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = captionInfo.getKeyFrameInfo();
long currentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
Log.d(TAG, " trimIn:" + timeStamp + " itemKey:" + next.getKey() + " timelinePosition:" + currentPosition);
if (next.getKey() < currentPosition) {
removeKeyFrameByCurrentTime(next.getKey());
Map<Long, KeyFrameInfo> keyFrameInfoHashMapAfter = captionInfo.getKeyFrameInfo();
for (Map.Entry<Long, KeyFrameInfo> longCaptionKeyFrameInfoEntry : entriesAfter) {
KeyFrameInfo captionKeyFrameInfo = longCaptionKeyFrameInfoEntry.getValue();
addKeyFrameOnCurrentTime(longCaptionKeyFrameInfoEntry.getKey() - mCurCaption.getInPoint(),
// ... 25 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-034` `rebuildBezierData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2044`

API classes: `NvsControlPointPair`
Common calls: `getInPoint()`, `getControlPoint()`, `setControlPoint()`, `getValue()`, `getForwardControlPointX()`, `getBackwardControlPointX()`, `getKey()`, `setCurrentKeyFrameTime()`, `getBackwardControlPointYForTransX()`, `getBackwardControlPointYForTransY()`, `getForwardControlPointYForTransX()`, `getForwardControlPointYForTransY()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> longCaptionKeyFrameInfoEntry : entriesAfter) {
KeyFrameInfo keyFrameInfo = longCaptionKeyFrameInfoEntry.getValue();
double forwardControlPointX = keyFrameInfo.getForwardControlPointX();
double backwardControlPointX = keyFrameInfo.getBackwardControlPointX();
long duration = longCaptionKeyFrameInfoEntry.getKey() - mCurCaption.getInPoint();
mCurCaption.setCurrentKeyFrameTime(duration);
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (backwardControlPointX != -1) {
pairX.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairX.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransX();
pairY.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairY.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransY();
if (forwardControlPointX != -1) {
pairX.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairX.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransX();
pairY.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairY.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransY();
mCurCaption.setControlPoint(TRANS_X, pairX);
mCurCaption.setControlPoint(TRANS_Y, pairY);
```

## `captions-stickers-035` `rebuildBezierData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2047`

API classes: `NvsControlPointPair`
Common calls: `getInPoint()`, `getControlPoint()`, `setControlPoint()`, `getValue()`, `getForwardControlPointX()`, `getBackwardControlPointX()`, `getKey()`, `setCurrentKeyFrameTime()`, `getBackwardControlPointYForTransX()`, `getBackwardControlPointYForTransY()`, `getForwardControlPointYForTransX()`, `getForwardControlPointYForTransY()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> longCaptionKeyFrameInfoEntry : entriesAfter) {
KeyFrameInfo keyFrameInfo = longCaptionKeyFrameInfoEntry.getValue();
double forwardControlPointX = keyFrameInfo.getForwardControlPointX();
double backwardControlPointX = keyFrameInfo.getBackwardControlPointX();
long duration = longCaptionKeyFrameInfoEntry.getKey() - mCurCaption.getInPoint();
mCurCaption.setCurrentKeyFrameTime(duration);
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (backwardControlPointX != -1) {
pairX.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairX.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransX();
pairY.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairY.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransY();
if (forwardControlPointX != -1) {
pairX.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairX.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransX();
pairY.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairY.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransY();
mCurCaption.setControlPoint(TRANS_X, pairX);
mCurCaption.setControlPoint(TRANS_Y, pairY);
```

## `captions-stickers-036` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2195`

API classes: `NvsTimelineCaption`, `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `isModular()`, `getNextCaption()`, `getFirstCaption()`, `getCategory()`, `getRoleInTheme()`, `e()`, `getInPoint()`, `getOutPoint()`, `setTraditional()`, `getTimeSpanshadowView()`, `setBackgroundColor()`, `getColor()`

Simple sequence:

```java
NvsTimelineCaption caption = mTimeline.getFirstCaption();
while (caption != null) {
int capCategory = caption.getCategory();
int roleTheme = caption.getRoleInTheme();
if (capCategory == NvsTimelineCaption.THEME_CATEGORY
&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作编辑处理
caption = mTimeline.getNextCaption(caption);
long inPoint = caption.getInPoint();
long outPoint = caption.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
timeSpanInfo.setTraditional(!caption.isModular());
timeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-037` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2197`

API classes: `NvsTimelineCaption`, `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `isModular()`, `getNextCaption()`, `getCategory()`, `getRoleInTheme()`, `e()`, `getInPoint()`, `getOutPoint()`, `setTraditional()`, `getTimeSpanshadowView()`, `setBackgroundColor()`, `getColor()`, `add()`

Simple sequence:

```java
while (caption != null) {
int capCategory = caption.getCategory();
int roleTheme = caption.getRoleInTheme();
if (capCategory == NvsTimelineCaption.THEME_CATEGORY
&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作编辑处理
caption = mTimeline.getNextCaption(caption);
long inPoint = caption.getInPoint();
long outPoint = caption.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
timeSpanInfo.setTraditional(!caption.isModular());
timeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-038` `selectCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2231`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `get()`, `getZValue()`, `setKeyFrameInfo()`, `setVisibility()`, `size()`, `getKeyFrameInfo()`, `getTimelineCurrentPosition()`, `getCaptionsByTimelinePosition()`, `e()`, `getCategory()`, `getRoleInTheme()`, `getVisibility()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineCaption> captionList = mTimeline.getCaptionsByTimelinePosition(curPos);
if (captionCount > 0) {
float zVal = captionList.get(0).getZValue();
for (int i = 0; i < captionCount; i++) {
float tmpZVal = captionList.get(i).getZValue();
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(currentCaptionInfo.getKeyFrameInfo());
if (mCurCaption.getCategory() == NvsTimelineCaption.THEME_CATEGORY
&& mCurCaption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
mCaptionStyleButton.setVisibility(View.GONE);
if (mLlKeyFrame.getVisibility() != View.VISIBLE) {
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
if (!mAddKeyFrame) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
mCaptionStyleButton.setVisibility(View.GONE);
if (mCurCaption != null) {
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
// ... 3 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-039` `selectCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2236`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `get()`, `getZValue()`, `setKeyFrameInfo()`, `setVisibility()`, `getKeyFrameInfo()`, `getCategory()`, `getRoleInTheme()`, `getVisibility()`, `isEmpty()`

Simple sequence:

```java
if (captionCount > 0) {
float zVal = captionList.get(0).getZValue();
for (int i = 0; i < captionCount; i++) {
float tmpZVal = captionList.get(i).getZValue();
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(currentCaptionInfo.getKeyFrameInfo());
if (mCurCaption.getCategory() == NvsTimelineCaption.THEME_CATEGORY
&& mCurCaption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
mCaptionStyleButton.setVisibility(View.GONE);
if (mLlKeyFrame.getVisibility() != View.VISIBLE) {
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
if (!mAddKeyFrame) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
mCaptionStyleButton.setVisibility(View.GONE);
```

## `captions-stickers-040` `selectTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2311`

API classes: `NvsTimelineTimeSpan`
Common calls: `get()`, `size()`, `selectTimeSpan()`

Simple sequence:

```java
if (captionTimeSpanInfo.mCaption == mCurCaption) {
NvsTimelineTimeSpan timeSpan = mTimeSpanInfoList.get(i).mTimeSpan;
```

## `captions-stickers-041` `selectTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2313`

API classes: `NvsTimelineTimeSpan`
Common calls: `get()`, `selectTimeSpan()`

Simple sequence:

```java
if (captionTimeSpanInfo.mCaption == mCurCaption) {
NvsTimelineTimeSpan timeSpan = mTimeSpanInfoList.get(i).mTimeSpan;
```

## `captions-stickers-042` `selectTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionActivity.java:2314`

API classes: `NvsTimelineTimeSpan`
Common calls: `get()`, `selectTimeSpan()`

Simple sequence:

```java
if (captionTimeSpanInfo.mCaption == mCurCaption) {
NvsTimelineTimeSpan timeSpan = mTimeSpanInfoList.get(i).mTimeSpan;
```

## `captions-stickers-043` `initTitle`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:434`

API classes: `NvsVideoTrack`
Common calls: `setVolumeGain()`, `dp2px()`, `getSystemService()`, `getVideoTrackByIndex()`, `post()`, `playVideo()`, `postDelayed()`, `getFonts()`

Simple sequence:

```java
(InputMethodManager) mContext.getSystemService(Context.INPUT_METHOD_SERVICE);
NvsVideoTrack videoTrackByIndex = mTimeline.getVideoTrackByIndex(0);
videoTrackByIndex.setVolumeGain(0, 0);
videoTrackByIndex.setVolumeGain(1, 1);
mPresenter.getFonts();
```

## `captions-stickers-044` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:653`

API classes: `NvsTimeline`
Common calls: `sendEmptyMessage()`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-045` `onTextChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:782`

API classes: `NvsCaptionSpan`
Common calls: `getEnd()`, `setEnd()`, `getStart()`, `remove()`, `size()`, `get()`, `setStart()`, `toString()`, `getSelectionStart()`, `e()`, `getTextSpanList()`, `setTextSpanList()`

Simple sequence:

```java
mAfterSelect = mEtCaptionInput.getSelectionStart();
if (mCurCaption != null) {
List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
for (int i = textSpanList.size() - 1; i >= 0; i--) {
NvsCaptionSpan nvsCaptionSpan = textSpanList.get(i);
int start = nvsCaptionSpan.getStart();
int end = nvsCaptionSpan.getEnd();
if (mBeforeSelect == end) {
nvsCaptionSpan.setEnd(mAfterSelect);
nvsCaptionSpan.setEnd(nvsCaptionSpan.getEnd() + offset);
nvsCaptionSpan.setStart(nvsCaptionSpan.getStart() + offset);
nvsCaptionSpan.setEnd(nvsCaptionSpan.getEnd() + offset);
for (int i = textSpanList.size() - 1; i >= 0; i--) {
NvsCaptionSpan nvsCaptionSpan = textSpanList.get(i);
int start = nvsCaptionSpan.getStart();
int end = nvsCaptionSpan.getEnd();
if (mBeforeSelect > start && mAfterSelect < end) {
nvsCaptionSpan.setEnd(nvsCaptionSpan.getEnd() + offset);
nvsCaptionSpan.setStart(nvsCaptionSpan.getStart() + offset);
mCurCaption.setTextSpanList(textSpanList);
currentCaptionInfo.setText("");
mTimeline.removeCaption(mCurCaption);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-046` `fontDownloadFail`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1263`

API classes: `NvsColor`, `NvsCaption`, `NvsTimelineCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `colorStringtoNvsColor()`, `setShadowColor()`, `isShadow()`, `setOutlineColor()`, `setOutlineWidth()`, `setBold()`, `setItalic()`, `setUnderline()`, `setUsedLetterSpacingFlag()`, `setLetterSpacing()`, `setLineSpacing()`, `getCaptionColorAlpha()`

Simple sequence:

```java
NvsTimelineCaption captionByIndex = null;
if (captionInfo != null) {
captionByIndex = getCaptionByIndex(captionInfo.getCaptionZVal());
if (bIsStyleUuidApplyToAll) {
captionInfo.setCaptionStyleUuid(curCaptionInfo.getCaptionStyleUuid());
if (captionByIndex != null) {
captionByIndex.applyCaptionStyle(curCaptionInfo.getCaptionStyleUuid());
if (bIsStyleUuidApplyToAllChange) {
captionInfo.setCaptionStyleUuid("");
if (captionByIndex != null) {
captionByIndex.applyCaptionStyle("");
if (bIsCaptionColorApplyToAll) {
captionInfo.setCaptionColor(curCaptionInfo.getCaptionColor());
captionInfo.setCaptionColorAlpha(curCaptionInfo.getCaptionColorAlpha());
captionInfo.setUsedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
if (captionByIndex != null) {
NvsColor color = ColorUtil.colorStringtoNvsColor(captionInfo.getCaptionColor());
color.a = captionInfo.getCaptionColorAlpha() / 100f;
captionByIndex.setTextColor(color);
if (captionByIndex != null) {
NvsColor captionColor = captionByIndex.getTextColor();
captionInfo.setCaptionColor(ColorUtil.nvsColorToHexString(captionColor));
captionInfo.setCaptionColorAlpha(captionInfo.getCaptionColorAlpha());
captionInfo.setUsedColorFlag(CaptionInfo.ATTRIBUTE_UNUSED_FLAG);
// ... 122 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-047` `updateCaptionPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:1509`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `getRoleInTheme()`, `getNextCaption()`

Simple sequence:

```java
&& caption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作处理
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-048` `applyAssemblyCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2564`

API classes: `NvsColor`
Common calls: `isEmpty()`, `playVideo()`, `setModularCaptionAnimationPeroid()`, `applyModularCaptionAnimation()`, `setCombinationAnimationUuid()`, `setCombinationAnimationDuration()`, `getModularCaptionOutAnimationDuration()`, `applyModularCaptionOutAnimation()`, `setModularCaptionOutAnimationDuration()`, `applyModularCaptionInAnimation()`, `setModularCaptionInAnimationDuration()`, `getModularCaptionAnimationPeroid()`

Simple sequence:

```java
long startTime = mCurCaption.getInPoint();
long endTime = mCurCaption.getOutPoint();
mVideoFragment.setDrawRectVisible(View.GONE);
mCurCaption.applyModularCaptionRenderer(asset.uuid);
if (captionInfo != null) {
captionInfo.setRichWordUuid(asset.uuid);
mCurCaption.applyModularCaptionContext(asset.uuid);
if (captionInfo != null) {
captionInfo.setBubbleUuid(asset.uuid);
if (!TextUtils.isEmpty(mCurCaption.getModularCaptionOutAnimationPackageId())) {
mCurCaption.applyModularCaptionOutAnimation("");
mCurCaption.setModularCaptionOutAnimationDuration(IN_OUT_ANIMATION_DEFAULT_DURATION);
if (!TextUtils.isEmpty(mCurCaption.getModularCaptionInAnimationPackageId())) {
mCurCaption.applyModularCaptionInAnimation("");
mCurCaption.setModularCaptionInAnimationDuration(IN_OUT_ANIMATION_DEFAULT_DURATION);
if (mCurCaption.getModularCaptionAnimationPeroid() == 0) {
mCurCaption.setModularCaptionAnimationPeroid(ANIMATION_DEFAULT_DURATION);
mCurCaption.applyModularCaptionAnimation(asset.uuid);
if (captionInfo != null) {
captionInfo.setCombinationAnimationUuid(asset.uuid);
captionInfo.setCombinationAnimationDuration(
mCurCaption.getModularCaptionAnimationPeroid());
captionInfo.setMarchOutAnimationUuid("");
captionInfo.setMarchInAnimationUuid("");
// ... 43 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-049` `initCaptionStyleFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2807`

API classes: `NvsCaptionSpan`, `NvsColor`
Static/constants: `NvsCaptionSpan.SPAN_TYPE_RENDER_ID`
Common calls: `get()`, `putInt()`, `getInstance()`, `getInPoint()`, `playVideo()`, `setCaptionStyleListener()`, `OnCaptionStyleListener()`, `applyToAllCaption()`, `setSelectedPos()`, `notifyDataSetChanged()`, `stopEngine()`, `jumpActivityForResult()`

Simple sequence:

```java
captionStyleFragment.setCaptionStyleListener(new CaptionStyleFragment.OnCaptionStyleListener() {
mCaptionStyleFragment.applyToAllCaption(bIsStyleUuidApplyToAll);
mCaptionStyleFragment.setSelectedPos(mSelectedStylePos);
AppManager.getInstance()
.jumpActivityForResult(AppManager.getInstance().currentActivity(),
long startTime = mCurCaption.getInPoint();
long endTime = mCurCaption.getOutPoint();
mVideoFragment.setDrawRectVisible(View.GONE);
NvAsset asset = mTotalCaptionStyleList.get(pos).getAsset();
mCurCaption.applyCaptionStyle(asset.uuid);
float captionSize = mCurCaption.getFontSize();
float scaleX = mCurCaption.getScaleX();
float scaleY = mCurCaption.getScaleY();
PointF pointF = mCurCaption.getCaptionTranslation();
float rotateAngle = mCurCaption.getRotationZ();
if (captionInfo != null) {
changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_RENDER_ID,
captionInfo.setCaptionStyleUuid(asset.uuid);
captionInfo.setTranslation(pointF);
captionInfo.setCaptionSize(captionSize);
captionInfo.setScaleFactorX(scaleX);
captionInfo.setScaleFactorY(scaleY);
captionInfo.setRotation(rotateAngle);
captionInfo.setBold(mCurCaption.getBold());
// ... 5 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-050` `initCaptionColorFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:2969`

API classes: `NvsCaptionSpan`, `NvsColorSpan`, `NvsColor`, `NvsOpacitySpan`, `NvsBodyOpacitySpan`
Static/constants: `NvsCaptionSpan.SPAN_TYPE_COLOR`, `NvsCaptionSpan.SPAN_TYPE_OPACITY`
Common calls: `get()`, `getTextSpanList()`, `notifyDataSetChanged()`, `updateCaptionOpacityValue()`, `setTextColor()`, `setUsedColorFlag()`, `setCaptionColor()`, `setCaptionColorListener()`, `OnCaptionColorListener()`, `applyToAllCaption()`, `setCaptionColorInfolist()`, `getCaptionColorAlpha()`

Simple sequence:

```java
captionColorFragment.setCaptionColorListener(new CaptionColorFragment.OnCaptionColorListener() {
mCaptionColorFragment.applyToAllCaption(bIsCaptionColorApplyToAll);
mCaptionColorFragment.setCaptionColorInfolist(mCaptionColorList);
if (index >= 0 && mCaptionDataListClone != null) {
mCaptionColorOpacityValue = mCaptionDataListClone.get(index).getCaptionColorAlpha();
NvsColor color = ColorUtil.colorStringtoNvsColor(mCaptionColorList.get(pos).mColorValue);
List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
NvsColorSpan nvsColorSpan = new NvsColorSpan(mSelectionStart, mSelectionEnd);
changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_COLOR,
mCurCaption.setTextColor(color);
if (captionInfo != null) {
captionInfo.setUsedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
captionInfo.setCaptionColor(mCaptionColorList.get(pos).mColorValue);
if (checkPosition()) {
List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
NvsBodyOpacitySpan nvsOpacitySpan =
new NvsBodyOpacitySpan(mSelectionStart, mSelectionEnd);
changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_OPACITY,
NvsColor curColor = mCurCaption.getTextColor();
mCurCaption.setTextColor(curColor);
if (index >= 0) {
mCaptionDataListClone.get(index).setUsedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setCaptionColor(strColor);
mCaptionDataListClone.get(index).setCaptionColorAlpha(progress);
```

## `captions-stickers-051` `initCaptionOutlineFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3106`

API classes: `NvsCaptionSpan`, `NvsNormalTextSpan`, `NvsOutlineWidthSpan`, `NvsColor`, `NvsOutlineColorSpan`, `NvsOutlineOpacitySpan`
Static/constants: `NvsCaptionSpan.SPAN_TYPE_OUTLINE_WIDTH`, `NvsCaptionSpan.SPAN_TYPE_NORMAL_TEXT`
Common calls: `get()`, `setDrawOutline()`, `setOutlineColor()`, `setOutlineWidth()`, `updateCaptionOutlineWidthValue()`, `updateCaptionOutlineOpacityValue()`, `getTextSpanList()`, `notifyDataSetChanged()`, `setUsedOutlineFlag()`, `setHasOutline()`, `setOutlineColorAlpha()`, `OnCaptionOutlineListener()`

Simple sequence:

```java
mCaptionOutlineFragment.applyToAllCaption(bIsOutlineApplyToAll);
mCaptionOutlineFragment.setCaptionOutlineInfolist(mCaptionOutlineColorList);
if (isDrawOutline) {
mCaptionOutlineWidthValue = mCaptionDataListClone.get(index).getOutlineWidth();
mCaptionDataListClone.get(index).getOutlineColorAlpha();
mCurCaption.setDrawOutline(false);
.setUsedOutlineFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setHasOutline(false);
mCaptionDataListClone.get(index).setOutlineColor("");
NvsColor color =
List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
NvsNormalTextSpan nvsNormalTextSpan =
new NvsNormalTextSpan(mSelectionStart, mSelectionEnd);
NvsOutlineWidthSpan nvsOutlineWidthSpan =
new NvsOutlineWidthSpan(mSelectionStart, mSelectionEnd);
NvsOutlineColorSpan nvsOutlineColorSpan =
new NvsOutlineColorSpan(mSelectionStart, mSelectionEnd);
mCurCaption.setDrawOutline(true);
mCurCaption.setOutlineColor(color);
mCurCaption.setOutlineWidth(mCaptionOutlineWidthValue);
.setUsedOutlineFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setHasOutline(true);
.setOutlineColor(mCaptionOutlineColorList.get(pos).mColorValue);
mCaptionDataListClone.get(index).setOutlineWidth(mCaptionOutlineWidthValue);
// ... 21 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-052` `initCaptionBackgroundFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3345`

API classes: `NvsColor`
Common calls: `get()`, `abs()`, `setUsedBackgroundFlag()`, `setCaptionBackground()`, `setBackgroundColor()`, `updateCaptionOpacityValue()`, `getBackgroundColor()`, `notifyDataSetChanged()`, `getTextBoundingRect()`, `initCaptionMaxCorner()`, `getBackgroundRadius()`, `updateCaptionCornerValue()`

Simple sequence:

```java
if (mCurCaption != null) {
mCaptionBackgroundFragment.applyToAllCaption(bIsCaptionBackgroundApplyToAll);
mCaptionDataListClone.get(index).getCaptionBackgroundAlpha();
NvsColor curColor = mCurCaption.getBackgroundColor();
mCaptionBackgroundFragment.setCaptionBackgroundInfolist(mCaptionBackgroundList);
RectF rectF = mCurCaption.getTextBoundingRect();
if (mCurCaption != null) {
mCaptionBackgroundCornerValue = mCurCaption.getBackgroundRadius();
if (mCurCaption != null) {
mCaptionBackgroundPeddingValue = mCurCaption.getBoundaryPaddingRatio();
NvsColor color = ColorUtil.colorStringtoNvsColor(noColor);
mCurCaption.setBackgroundColor(color);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setCaptionBackground(noColor);
NvsColor color =
mCurCaption.setBackgroundColor(color);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
.setCaptionBackground(mCaptionBackgroundList.get(pos).mColorValue);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
.setCaptionBackground(mCaptionBackgroundList.get(pos).mColorValue);
mCaptionBackgroundCornerValue = mCurCaption.getBackgroundRadius();
NvsColor curColor = mCurCaption.getBackgroundColor();
mCurCaption.setBackgroundColor(curColor);
if (captionInfo != null) {
// ... 10 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-053` `onFragmentLoadFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3351`

API classes: `NvsColor`
Common calls: `get()`, `abs()`, `applyToAllCaption()`, `getCaptionBackgroundAlpha()`, `updateCaptionOpacityValue()`, `getBackgroundColor()`, `setCaptionBackgroundInfolist()`, `notifyDataSetChanged()`, `getTextBoundingRect()`, `initCaptionMaxCorner()`, `getBackgroundRadius()`, `updateCaptionCornerValue()`

Simple sequence:

```java
if (mCurCaption != null) {
mCaptionBackgroundFragment.applyToAllCaption(bIsCaptionBackgroundApplyToAll);
mCaptionDataListClone.get(index).getCaptionBackgroundAlpha();
NvsColor curColor = mCurCaption.getBackgroundColor();
mCaptionBackgroundFragment.setCaptionBackgroundInfolist(mCaptionBackgroundList);
RectF rectF = mCurCaption.getTextBoundingRect();
if (mCurCaption != null) {
mCaptionBackgroundCornerValue = mCurCaption.getBackgroundRadius();
if (mCurCaption != null) {
mCaptionBackgroundPeddingValue = mCurCaption.getBoundaryPaddingRatio();
```

## `captions-stickers-054` `onCaptionColor`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3393`

API classes: `NvsColor`
Common calls: `get()`, `setUsedBackgroundFlag()`, `setCaptionBackground()`, `colorStringtoNvsColor()`, `setBackgroundColor()`, `size()`, `notifyDataSetChanged()`, `updateCaptionOpacityValue()`, `getBackgroundRadius()`, `updateCaptionCornerValue()`

Simple sequence:

```java
NvsColor color = ColorUtil.colorStringtoNvsColor(noColor);
mCurCaption.setBackgroundColor(color);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setCaptionBackground(noColor);
NvsColor color =
mCurCaption.setBackgroundColor(color);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
.setCaptionBackground(mCaptionBackgroundList.get(pos).mColorValue);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
.setCaptionBackground(mCaptionBackgroundList.get(pos).mColorValue);
mCaptionBackgroundCornerValue = mCurCaption.getBackgroundRadius();
```

## `captions-stickers-055` `initCaptionLetterSpacingFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3853`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setSelectedStandard()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`, `setSelectedMore()`, `setSelectedLarge()`, `setSelectedSmall()`, `OnCaptionLetterSpacingListener()`, `applyToAllCaption()`, `getLetterSpacing()`

Simple sequence:

```java
mCaptionLetterSpacingFragment.applyToAllCaption(bIsLetterSpacingApplyToAll);
float letterSpaceing = mCurCaption.getLetterSpacing();
if (letterSpaceing == getLetterSpacing(CAPTION_PERCENT_STANDARD_SPACING)) {
mCaptionLetterSpacingFragment.setSelectedStandard(
mCaptionLetterSpacingFragment.setSelectedMore(
mCaptionLetterSpacingFragment.setSelectedLarge(
mCaptionLetterSpacingFragment.setSelectedSmall(
mCaptionLetterSpacingFragment.setSelectedStandard(
float lineSpacing = mCurCaption.getLineSpacing();
if (lineSpacing == CAPTION_SMALL_LINE_SPACING) {
mCaptionLetterSpacingFragment.setSelectedSmall(
mCaptionLetterSpacingFragment.setSelectedStandard(
mCaptionLetterSpacingFragment.setSelectedMore(
mCaptionLetterSpacingFragment.setSelectedLarge(
mCaptionLetterSpacingFragment.setSelectedStandard(
mCurCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurCaption.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
mCurCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
// ... 23 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-056` `onSmallBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3902`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurCaption.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
```

## `captions-stickers-057` `onStandardBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3938`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurCaption.setLineSpacing(CAPTION_STANDARD_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_STANDARD_LINE_SPACING);
```

## `captions-stickers-058` `onMoreBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:3975`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurCaption.setLineSpacing(CAPTION_MORE_LARGE_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_MORE_LARGE_LINE_SPACING);
```

## `captions-stickers-059` `onLargeBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4011`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurCaption.setLineSpacing(CAPTION_LARGE_LINE_SPACEING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_LARGE_LINE_SPACEING);
```

## `captions-stickers-060` `initCaptionFontSizeRatioFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4265`

API classes: `NvsFontSizeRatioSpan`, `NvsCaptionSpan`
Common calls: `setSeekEnable()`, `get()`, `OnCaptionFontSizeRationListener()`, `isFrameCaption()`, `applyToAllCaption()`, `getCaptionSize()`, `round()`, `updateCaptionOpacityValue()`, `getTextSpanList()`, `setFontSize()`, `setCaptionSize()`

Simple sequence:

```java
if (checkPosition()) {
mCaptionFontSizeRatioFragment.setSeekEnable(true);
mCaptionFontSizeRatioFragment.setSeekEnable(!frameCaption);
captionFontSizeRatioFragment.applyToAllCaption(false);
float captionSize = captionInfo.getCaptionSize();
List<NvsCaptionSpan> textSpanList = mCurCaption.getTextSpanList();
NvsFontSizeRatioSpan nvsFontSizeRatioSpan =
new NvsFontSizeRatioSpan(mSelectionStart, mSelectionEnd);
mCurCaption.setFontSize(fontSize);
captionInfo.setCaptionSize(fontSize);
```

## `captions-stickers-061` `initCaptionShadowFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4343`

API classes: `NvsCaptionSpan`, `NvsShadowOpacitySpan`, `NvsColor`
Static/constants: `NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY`
Common calls: `get()`, `setShadowColor()`, `showSeekContainerVisible()`, `setDrawShadow()`, `notifyDataSetChanged()`, `updateCaptionOpacityValue()`, `setShadowOpacity()`, `size()`, `getTextSpanList()`, `getShadowColor()`, `setCaptionShadowColor()`, `setShadow()`

Simple sequence:

```java
captionShadowFragment.applyToAllCaption(false);
if (captionInfo != null) {
float shadowOpacity = captionInfo.getShadowOpacity();
changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY,
NvsColor shadowColor = mCurCaption.getShadowColor();
mCurCaption.setShadowColor(shadowColor);
captionInfo.setShadowOpacity(progress / 100f);
mCurCaption.setDrawShadow(false);
captionInfo.setShadowColor("");
captionInfo.setShadowOpacity(0.0f);
captionInfo.setShadow(false);
captionInfo.setUsedShadowFlag(CaptionInfo.ATTRIBUTE_UNUSED_FLAG);
changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY,
mCurCaption.setDrawShadow(true);
NvsColor color =
mCurCaption.setShadowOffset(point);
mCurCaption.setShadowColor(color);
captionInfo.setShadowColor(mCaptionShadowList.get(pos).mColorValue);
captionInfo.setShadowOpacity(1.0f);
captionInfo.setShadow(true);
captionInfo.setUsedShadowFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
```

## `captions-stickers-062` `onChangeShadow`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4372`

API classes: `NvsCaptionSpan`, `NvsShadowOpacitySpan`, `NvsColor`
Static/constants: `NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY`
Common calls: `get()`, `setShadowColor()`, `getShadowColor()`, `getTextSpanList()`, `setMisShadowOpacity()`, `setShadowOpacity()`

Simple sequence:

```java
changeOrRemoveSpanByType(NvsCaptionSpan.SPAN_TYPE_SHADOW_OPACITY,
NvsColor shadowColor = mCurCaption.getShadowColor();
mCurCaption.setShadowColor(shadowColor);
captionInfo.setShadowOpacity(progress / 100f);
```

## `captions-stickers-063` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4803`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timestamp,
NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-064` `getCurCaptionZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:4932`

API classes: `NvsTimelineCaption`
Common calls: `getFirstCaption()`, `getZValue()`, `getNextCaption()`

Simple sequence:

```java
NvsTimelineCaption caption = mTimeline.getFirstCaption();
while (caption != null) {
float tmpZVal = caption.getZValue();
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-065` `setSpanValue`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5047`

API classes: `NvsFontFamilySpan`

Simple sequence:

```java
} else if (nvsCaptionSpan instanceof NvsFontFamilySpan) {
```

## `captions-stickers-066` `changeOrRemoveSpanByType`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5081`

API classes: `NvsCaptionSpan`
Common calls: `equals()`, `getEnd()`, `remove()`, `setEnd()`, `size()`, `get()`, `getStart()`, `getType()`, `setStart()`, `add()`

Simple sequence:

```java
for (int i = textSpanList.size() - 1; i >= 0; i--) {
NvsCaptionSpan nvsCaptionSpan = textSpanList.get(i);
int start = nvsCaptionSpan.getStart();
int end = nvsCaptionSpan.getEnd();
String spanType = nvsCaptionSpan.getType();
nvsCaptionSpan.setEnd(mSelectionStart);
nvsCaptionSpan.setStart(mSelectionEnd);
NvsCaptionSpan spanByType = createSpanByType(type, mSelectionEnd, nvsCaptionSpan.getEnd());
nvsCaptionSpan.setEnd(mSelectionStart);
```

## `captions-stickers-067` `createSpanByType`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/CaptionStyleActivity.java:5162`

API classes: `NvsCaptionSpan`
Static/constants: `NvsCaptionSpan.SPAN_TYPE_COLOR`
Common calls: `equals()`

Simple sequence:

```java
} else if (NvsCaptionSpan.SPAN_TYPE_COLOR.equals(type)) {
```

## `captions-stickers-068` `convertFontData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/presenter/CaptionPresenter.java:102`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `isEmpty()`, `getRemotePackageUrl()`, `getCoverUrl()`, `getDisplayName()`, `getUuid()`, `getInstance()`, `registerFontByFilePath()`, `setAsset()`, `setAssetMode()`, `add()`

Simple sequence:

```java
item.coverUrl = fileInfo.getCoverUrl();
item.fxFileName = fileInfo.getDisplayName();
item.uuid = fileInfo.getUuid();
item.remotePackageUrl = fileInfo.getRemotePackageUrl();
item.localDirPath = getFontLocalDirPath(fileInfo.getRemotePackageUrl());
if (!TextUtils.isEmpty(item.localDirPath)) {
item.name = NvsStreamingContext.getInstance().registerFontByFilePath(item.localDirPath);
localFontInfo.setAsset(item);
localFontInfo.setAssetMode(AssetItem.ASSET_LOCAL);
```

## `captions-stickers-069` `convertFontData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/presenter/CaptionPresenter.java:103`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `isEmpty()`, `getRemotePackageUrl()`, `getCoverUrl()`, `getDisplayName()`, `getUuid()`, `getInstance()`, `registerFontByFilePath()`, `setAsset()`, `setAssetMode()`, `add()`

Simple sequence:

```java
item.coverUrl = fileInfo.getCoverUrl();
item.fxFileName = fileInfo.getDisplayName();
item.uuid = fileInfo.getUuid();
item.remotePackageUrl = fileInfo.getRemotePackageUrl();
item.localDirPath = getFontLocalDirPath(fileInfo.getRemotePackageUrl());
if (!TextUtils.isEmpty(item.localDirPath)) {
item.name = NvsStreamingContext.getInstance().registerFontByFilePath(item.localDirPath);
localFontInfo.setAsset(item);
localFontInfo.setAssetMode(AssetItem.ASSET_LOCAL);
```

## `captions-stickers-070` `convertFontData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/Caption/presenter/CaptionPresenter.java:106`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getRemotePackageUrl()`, `getCoverUrl()`, `getDisplayName()`, `getUuid()`, `isEmpty()`, `getInstance()`, `registerFontByFilePath()`, `setAsset()`, `setAssetMode()`, `add()`

Simple sequence:

```java
item.coverUrl = fileInfo.getCoverUrl();
item.fxFileName = fileInfo.getDisplayName();
item.uuid = fileInfo.getUuid();
item.remotePackageUrl = fileInfo.getRemotePackageUrl();
item.localDirPath = getFontLocalDirPath(fileInfo.getRemotePackageUrl());
if (!TextUtils.isEmpty(item.localDirPath)) {
item.name = NvsStreamingContext.getInstance().registerFontByFilePath(item.localDirPath);
localFontInfo.setAsset(item);
localFontInfo.setAssetMode(AssetItem.ASSET_LOCAL);
```

## `captions-stickers-071` `initDrawRectListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:615`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getTimelineCurrentPosition()`, `getDrawRect()`, `mapViewToCanonical()`, `beforeTransitionCouldDo()`, `translateCaption()`, `setRegion()`, `getStreamingEngineState()`, `stop()`, `setupInputCacheForCaption()`, `translateAnimatedSticker()`, `instance()`, `getVideoFx()`

Simple sequence:

```java
if (mStreamingContext.getStreamingEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mStreamingContext.stop();
PointF pre = mLiveWindow.mapViewToCanonical(prePointF);
PointF p = mLiveWindow.mapViewToCanonical(nowPointF);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
if (!checkInLiveWindow(mDrawRect.getDrawRect())) {
updateWaterMarkPositionOnDrag(nowPointF.x - prePointF.x, prePointF.y - nowPointF.y, mDrawRect.getDrawRect());
if (!checkInLiveWindow(mDrawRect.getDrawRect())) {
updateEffectPositionOnDrag(nowPointF.x - prePointF.x, prePointF.y - nowPointF.y, mDrawRect.getDrawRect());
nvsTimelineVideoFx.setRegion(fx);
VideoFx videoFx = TimelineData.instance().getVideoFx();
if (videoFx != null) {
videoFx.setRegion(fx);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-072` `onScaleXandY`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:801`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `setRegion()`, `setPicturePath()`, `getDrawRect()`, `instance()`, `getVideoFx()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mDrawRect != null) {
mDrawRect.setPicturePath("");
updateWaterMarkPositionOnXAndY(xScaleFactor, yScaleFactor, anchor, mDrawRect.getDrawRect());
nvsTimelineVideoFx.setRegion(fx);
VideoFx videoFx = TimelineData.instance().getVideoFx();
if (videoFx != null) {
videoFx.setRegion(fx);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-073` `onScaleXandY`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:802`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `setRegion()`, `setPicturePath()`, `getDrawRect()`, `instance()`, `getVideoFx()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mDrawRect != null) {
mDrawRect.setPicturePath("");
updateWaterMarkPositionOnXAndY(xScaleFactor, yScaleFactor, anchor, mDrawRect.getDrawRect());
nvsTimelineVideoFx.setRegion(fx);
VideoFx videoFx = TimelineData.instance().getVideoFx();
if (videoFx != null) {
videoFx.setRegion(fx);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-074` `onAlignClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:839`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT`, `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER`, `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setTextAlignment()`, `getTextAlignment()`, `getTimelineCurrentPosition()`, `onAssetAlign()`

Simple sequence:

```java
switch (mCurCaption.getTextAlignment()) {
case NvsTimelineCaption.TEXT_ALIGNMENT_LEFT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_CENTER);  //居中对齐 Center alignment
case NvsTimelineCaption.TEXT_ALIGNMENT_CENTER:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT);  //居右或者居上对齐 Align to the right or top
case NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_LEFT);  //居左或者居下对齐 Align left or bottom
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (mAssetEditListener != null) {
mAssetEditListener.onAssetAlign(mCurCaption.getTextAlignment());
```

## `captions-stickers-075` `onAlignClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:840`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.TEXT_ALIGNMENT_LEFT`, `NvsTimelineCaption.TEXT_ALIGNMENT_CENTER`, `NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT`
Common calls: `setTextAlignment()`, `getTextAlignment()`

Simple sequence:

```java
switch (mCurCaption.getTextAlignment()) {
case NvsTimelineCaption.TEXT_ALIGNMENT_LEFT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_CENTER);  //居中对齐 Center alignment
case NvsTimelineCaption.TEXT_ALIGNMENT_CENTER:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT);  //居右或者居上对齐 Align to the right or top
case NvsTimelineCaption.TEXT_ALIGNMENT_RIGHT:
mCurCaption.setTextAlignment(NvsTimelineCaption.TEXT_ALIGNMENT_LEFT);  //居左或者居下对齐 Align left or bottom
```

## `captions-stickers-076` `onOrientationChange`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:863`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setVerticalLayout()`, `getTimelineCurrentPosition()`, `onOrientationChange()`

Simple sequence:

```java
if (mCurCaption != null) {
mCurCaption.setVerticalLayout(!isHorizontal);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-077` `onOrientationChange`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:864`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setVerticalLayout()`, `getTimelineCurrentPosition()`, `onOrientationChange()`

Simple sequence:

```java
if (mCurCaption != null) {
mCurCaption.setVerticalLayout(!isHorizontal);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-078` `onOrientationChange`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:866`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setVerticalLayout()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mCurCaption != null) {
mCurCaption.setVerticalLayout(!isHorizontal);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-079` `onHorizontalFlipClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:878`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getHorizontalFlip()`, `setHorizontalFlip()`, `getTimelineCurrentPosition()`, `onAssetHorizFlip()`

Simple sequence:

```java
boolean isHorizontalFlip = !mCurAnimateSticker.getHorizontalFlip();
mCurAnimateSticker.setHorizontalFlip(isHorizontalFlip);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-080` `onHorizontalFlipClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:879`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getHorizontalFlip()`, `setHorizontalFlip()`, `getTimelineCurrentPosition()`, `onAssetHorizFlip()`

Simple sequence:

```java
boolean isHorizontalFlip = !mCurAnimateSticker.getHorizontalFlip();
mCurAnimateSticker.setHorizontalFlip(isHorizontalFlip);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-081` `updateThemeCaptionCoordinate`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1327`

API classes: `NvsTimelineCaption`
Common calls: `size()`, `getBoundingRectangleVertices()`, `mapCanonicalToView()`, `get()`, `add()`, `setDrawRect()`

Simple sequence:

```java
public void updateThemeCaptionCoordinate(NvsTimelineCaption caption) {
List<PointF> list = caption.getBoundingRectangleVertices();
for (int i = 0; i < list.size(); i++) {
PointF pointF = mLiveWindow.mapCanonicalToView(list.get(i));
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_THEMECAPTION);
```

## `captions-stickers-082` `setCurCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1360`

API classes: `NvsCaption`
Common calls: `e()`, `getBackgroundRadius()`

Simple sequence:

```java
public void setCurCaption(NvsCaption caption) {
if (null != caption) {
Log.e("mCurCaption", "===" + mCurCaption.getBackgroundRadius());
```

## `captions-stickers-083` `updateCaptionCoordinate`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1375`

API classes: `NvsCaption`
Static/constants: `NvsCaption.BOUNDING_TYPE_FRAME`
Common calls: `getCaptionBoundingVertices()`, `size()`, `setHorizontal()`, `getVerticalLayout()`, `setDrawRect()`

Simple sequence:

```java
public void updateCaptionCoordinate(NvsCaption caption) {
List<PointF> list = caption.getCaptionBoundingVertices(NvsCaption.BOUNDING_TYPE_FRAME);
mDrawRect.setHorizontal(!caption.getVerticalLayout());
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_CAPTION);
```

## `captions-stickers-084` `updateCaptionCoordinate`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1376`

API classes: `NvsCaption`
Static/constants: `NvsCaption.BOUNDING_TYPE_FRAME`
Common calls: `getCaptionBoundingVertices()`, `size()`, `setHorizontal()`, `getVerticalLayout()`, `setDrawRect()`

Simple sequence:

```java
List<PointF> list = caption.getCaptionBoundingVertices(NvsCaption.BOUNDING_TYPE_FRAME);
mDrawRect.setHorizontal(!caption.getVerticalLayout());
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_CAPTION);
```

## `captions-stickers-085` `setCurCompoundCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1395`

API classes: `NvsTimelineCompoundCaption`

Simple sequence:

```java
public NvsTimelineCompoundCaption getCurrCompoundCaption() {
```

## `captions-stickers-086` `updateCompoundCaptionCoordinate`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1403`

API classes: `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`, `NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT`
Common calls: `size()`, `getCompoundBoundingVertices()`, `getCaptionCount()`, `getCaptionBoundingVertices()`, `add()`, `setCompoundDrawRect()`

Simple sequence:

```java
public void updateCompoundCaptionCoordinate(NvsTimelineCompoundCaption caption) {
List<PointF> list = caption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);
int subCaptionCount = caption.getCaptionCount();
for (int index = 0; index < subCaptionCount; index++) {
List<PointF> subList = caption.getCaptionBoundingVertices(index, NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT);
mDrawRect.setCompoundDrawRect(newList, newSubCaptionList, Constants.EDIT_MODE_COMPOUND_CAPTION);
```

## `captions-stickers-087` `updateCompoundCaptionCoordinate`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1404`

API classes: `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`, `NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT`
Common calls: `size()`, `getCompoundBoundingVertices()`, `getCaptionCount()`, `getCaptionBoundingVertices()`, `add()`, `setCompoundDrawRect()`

Simple sequence:

```java
List<PointF> list = caption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);
int subCaptionCount = caption.getCaptionCount();
for (int index = 0; index < subCaptionCount; index++) {
List<PointF> subList = caption.getCaptionBoundingVertices(index, NvsTimelineCompoundCaption.BOUNDING_TYPE_TEXT);
mDrawRect.setCompoundDrawRect(newList, newSubCaptionList, Constants.EDIT_MODE_COMPOUND_CAPTION);
```

## `captions-stickers-088` `selectCompoundCaptionByHandClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1439`

API classes: `NvsTimelineCompoundCaption`
Static/constants: `NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME`
Common calls: `size()`, `getCompoundCaptionsByTimelinePosition()`, `getTimelineCurrentPosition()`, `get()`, `getCompoundBoundingVertices()`, `clickPointIsInnerDrawRect()`, `setDrawRect()`

Simple sequence:

```java
if (mTimeline == null) {
List<NvsTimelineCompoundCaption> captionList = mTimeline.getCompoundCaptionsByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));
for (int j = 0; j < captionList.size(); j++) {
NvsTimelineCompoundCaption caption = captionList.get(j);
List<PointF> list = caption.getCompoundBoundingVertices(NvsTimelineCompoundCaption.BOUNDING_TYPE_FRAME);
if (isSelected) {
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_COMPOUND_CAPTION);
```

## `captions-stickers-089` `selectCaptionByHandClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1737`

API classes: `NvsTimelineCaption`
Common calls: `size()`, `getCaptionsByTimelinePosition()`, `getTimelineCurrentPosition()`, `get()`, `getBoundingRectangleVertices()`, `clickPointIsInnerDrawRect()`, `setHorizontal()`, `getVerticalLayout()`, `setDrawRect()`

Simple sequence:

```java
if (mTimeline == null) {
List<NvsTimelineCaption> captionList = mTimeline.getCaptionsByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));
for (int j = 0; j < captionList.size(); j++) {
NvsTimelineCaption caption = captionList.get(j);
List<PointF> list = caption.getBoundingRectangleVertices();
if (isSelected) {
mDrawRect.setHorizontal(!caption.getVerticalLayout());
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_CAPTION);
```

## `captions-stickers-090` `setRecording`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1771`

API classes: `NvsAnimatedSticker`

Simple sequence:

```java
public void setCurAnimateSticker(NvsAnimatedSticker animateSticker) {
```

## `captions-stickers-091` `updateAnimateStickerCoordinate`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1789`

API classes: `NvsAnimatedSticker`
Common calls: `swap()`, `getBoundingRectangleVertices()`, `size()`, `getHorizontalFlip()`, `setDrawRect()`

Simple sequence:

```java
public void updateAnimateStickerCoordinate(NvsAnimatedSticker animateSticker) {
List<PointF> list = animateSticker.getBoundingRectangleVertices();
boolean isHorizonFlip = animateSticker.getHorizontalFlip();
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_STICKER);
```

## `captions-stickers-092` `selectAnimateStickerByHandClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1826`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `size()`, `getAnimatedStickersByTimelinePosition()`, `getTimelineCurrentPosition()`, `get()`, `getBoundingRectangleVertices()`, `clickPointIsInnerDrawRect()`, `setDrawRect()`

Simple sequence:

```java
if (mTimeline == null) {
List<NvsTimelineAnimatedSticker> stickerList = mTimeline.getAnimatedStickersByTimelinePosition(mStreamingContext.getTimelineCurrentPosition(mTimeline));
for (int j = 0; j < stickerList.size(); j++) {
NvsTimelineAnimatedSticker sticker = stickerList.get(j);
List<PointF> list = sticker.getBoundingRectangleVertices();
if (isSelected) {
mDrawRect.setDrawRect(newList, Constants.EDIT_MODE_STICKER);
```

## `captions-stickers-093` `isSelectedCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1978`

API classes: `NvsTimelineCaption`, `NvsClipCaption`
Common calls: `getInPoint()`, `getOutPoint()`

Simple sequence:

```java
if (mCurCaption instanceof NvsTimelineCaption) {
inPoint = ((NvsTimelineCaption) mCurCaption).getInPoint();
outPoint = ((NvsTimelineCaption) mCurCaption).getOutPoint();
} else if (mCurCaption instanceof NvsClipCaption) {
inPoint = ((NvsClipCaption) mCurCaption).getInPoint();
outPoint = ((NvsClipCaption) mCurCaption).getOutPoint();
```

## `captions-stickers-094` `isSelectedAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/VideoFragment.java:1996`

API classes: `NvsClipAnimatedSticker`, `NvsTimelineAnimatedSticker`
Common calls: `getInPoint()`, `getOutPoint()`

Simple sequence:

```java
if (mCurAnimateSticker instanceof NvsClipAnimatedSticker) {
inPoint = ((NvsClipAnimatedSticker) mCurAnimateSticker).getInPoint();
outPoint = ((NvsClipAnimatedSticker) mCurAnimateSticker).getOutPoint();
} else if (mCurAnimateSticker instanceof NvsTimelineAnimatedSticker) {
inPoint = ((NvsTimelineAnimatedSticker) mCurAnimateSticker).getInPoint();
outPoint = ((NvsTimelineAnimatedSticker) mCurAnimateSticker).getOutPoint();
```

## `captions-stickers-095` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/anim/AnimationActivity.java:138`

API classes: `NvsTimeline`
Common calls: `setOnClickListener()`, `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `setDrawRectVisible()`, `setAssetEditListener()`, `AssetEditListener()`, `setThemeCaptionSeekListener()`, `OnThemeCaptionSeekListener()`

Simple sequence:

```java
mAnimationAssetFinish.setOnClickListener(this);
mVideoFragment.setVideoFragmentCallBack(new VideoFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
mVideoFragment.setDrawRectVisible(View.GONE);
mVideoFragment.setAssetEditListener(new VideoFragment.AssetEditListener() {
mVideoFragment.setThemeCaptionSeekListener(new VideoFragment.OnThemeCaptionSeekListener() {
mAnimationInLayout.setOnClickListener(this);
mAnimationOutLayout.setOnClickListener(this);
mAnimationCompanyLayout.setOnClickListener(this);
mBottomLayout.setOnClickListener(this);
```

## `captions-stickers-096` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:412`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setTimelineScaleForSeek()`, `getDurationWidth()`, `getInstance()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (action == MotionEvent.ACTION_DOWN) {
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-097` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:429`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-098` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:451`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `get()`, `setIsStickerInPlay()`, `size()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoPlay.setBackgroundResource(R.mipmap.icon_edit_pause);
mAssetFragmentsArray.get(mCurTabPage).setIsStickerInPlay(true);
mVideoPlay.setBackgroundResource(R.mipmap.icon_edit_play);
for (int index = 0; index < tapCount; ++index) {
mAssetFragmentsArray.get(index).setIsStickerInPlay(false);
```

## `captions-stickers-099` `updateAllStickerPos`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:642`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `getInPoint()`, `removeKeyframeAtTime()`, `getTimelineCurrentPosition()`, `getAnimatedStickersByTimelinePosition()`, `getZValue()`, `get()`, `getKeyFrameInfoHashMap()`, `isEmpty()`, `setCurrentKeyFrameTime()`, `keySet()`, `contains()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineAnimatedSticker> animateStickerList = mTimeline.getAnimatedStickersByTimelinePosition(curPos);
for (NvsTimelineAnimatedSticker nvsTimelineAnimatedSticker : animateStickerList) {
int zVal = (int) nvsTimelineAnimatedSticker.getZValue();
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = stickerInfo.getKeyFrameInfoHashMap();
nvsTimelineAnimatedSticker.setCurrentKeyFrameTime(curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker TransX", curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker TransY", curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker Scale", curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker RotZ", curPos - nvsTimelineAnimatedSticker.getInPoint());
```

## `captions-stickers-100` `updateAllStickerPos`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:645`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `getInPoint()`, `removeKeyframeAtTime()`, `getZValue()`, `get()`, `getKeyFrameInfoHashMap()`, `isEmpty()`, `setCurrentKeyFrameTime()`, `keySet()`, `contains()`

Simple sequence:

```java
for (NvsTimelineAnimatedSticker nvsTimelineAnimatedSticker : animateStickerList) {
int zVal = (int) nvsTimelineAnimatedSticker.getZValue();
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = stickerInfo.getKeyFrameInfoHashMap();
nvsTimelineAnimatedSticker.setCurrentKeyFrameTime(curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker TransX", curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker TransY", curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker Scale", curPos - nvsTimelineAnimatedSticker.getInPoint());
nvsTimelineAnimatedSticker.removeKeyframeAtTime("Sticker RotZ", curPos - nvsTimelineAnimatedSticker.getInPoint());
```

## `captions-stickers-101` `updateAllKeyFrameViewStatusWhenScroll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:710`

API classes: `NvsTimelineTimeSpan`
Common calls: `setEnabled()`, `getKey()`, `isEmpty()`, `entrySet()`, `keySet()`, `toArray()`, `setCurrentTimelinePosition()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (beforeKeyFrame == -1 || ((objects != null) && ((long) (objects[0]) == timeStamp))) {
mBeforeKeyFrameView.setEnabled(false);
mBeforeKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1 || ((objects != null) && ((long) (objects[objects.length - 1]) == timeStamp))) {
mNextKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
if (timeStamp >= entry.getKey() - 100000 && timeStamp <= entry.getKey() + 100000) {
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentTimeSpan != null) {
currentTimeSpan.setCurrentTimelinePosition(timeStamp);
mBeforeKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(false);
```

## `captions-stickers-102` `updateAllKeyFrameViewStatusWhenScroll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:712`

API classes: `NvsTimelineTimeSpan`
Common calls: `setEnabled()`, `getKey()`, `entrySet()`, `keySet()`, `toArray()`, `setCurrentTimelinePosition()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (beforeKeyFrame == -1 || ((objects != null) && ((long) (objects[0]) == timeStamp))) {
mBeforeKeyFrameView.setEnabled(false);
mBeforeKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1 || ((objects != null) && ((long) (objects[objects.length - 1]) == timeStamp))) {
mNextKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
if (timeStamp >= entry.getKey() - 100000 && timeStamp <= entry.getKey() + 100000) {
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentTimeSpan != null) {
currentTimeSpan.setCurrentTimelinePosition(timeStamp);
mBeforeKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(false);
```

## `captions-stickers-103` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:801`

API classes: `NvsTimelineTimeSpan`
Common calls: `setVisibility()`, `getTimelineCurrentPosition()`, `getKeyFrameInfoHashMap()`, `getInPoint()`, `stopEngine()`, `setKeyFrameInfo()`, `setDrawRectVisible()`, `setEnabled()`, `removeAllKeyframe()`, `removeKeyframeAtTime()`, `d()`, `get()`

Simple sequence:

```java
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = currentStickerInfo.getKeyFrameInfoHashMap();
long currentTimelinePosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1) {
mNextKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(true);
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = currentStickerInfo.getKeyFrameInfoHashMap();
long currentTimelinePosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1) {
mBeforeKeyFrameView.setEnabled(false);
mBeforeKeyFrameView.setEnabled(true);
mDeleteAllKeyFrameTips.setOnBtnClickListener(new TipsDialog.OnBtnClickListener() {
if (mCurSelectAnimatedSticker != null) {
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransX");
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransY");
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker Scale");
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker RotZ");
stickerRemoveAllFrameView.setVisibility(View.GONE);
removeFirst.setVisibility(View.GONE);
currentStickerInfo.getKeyFrameInfoHashMap().clear();
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
// ... 70 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-104` `selectAnimateStickerByZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1202`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `size()`, `get()`, `getTimelineCurrentPosition()`, `getAnimatedStickersByTimelinePosition()`, `getZValue()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineAnimatedSticker> animateStickerList = mTimeline.getAnimatedStickersByTimelinePosition(curPos);
for (int i = 0; i < animateStickerList.size(); i++) {
int tmpZVal = (int) animateStickerList.get(i).getZValue();
```

## `captions-stickers-105` `applyAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1449`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `get()`, `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`, `addAnimatedSticker()`, `setZValue()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
mAddAnimateSticker = mTimeline.addAnimatedSticker(mInPoint, mStickerDuration,
mAddAnimateSticker.setZValue(zStickerVal);
```

## `captions-stickers-106` `applyAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1452`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-107` `applyAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1454`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-108` `applyCustomAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1493`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `get()`, `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`, `lastIndexOf()`, `substring()`, `toLowerCase()`, `equals()`, `exists()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-109` `applyCustomAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1496`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-110` `applyCustomAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1498`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-111` `addTimeSpanAndPlayVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1594`

API classes: `NvsTimelineTimeSpan`
Common calls: `get()`, `add()`, `setSelectedPos()`, `notifyDataSetChanged()`, `AnimateStickerTimeSpanInfo()`, `setCustomSticker()`, `setCustomImagePath()`, `setDrawRectVisible()`, `playVideo()`

Simple sequence:

```java
if (mPrevTabPage != mCurTabPage) {
mAssetFragmentsArray.get(mPrevTabPage).setSelectedPos(-1);
NvsTimelineTimeSpan timeSpan = addTimeSpan(mInPoint, endTime);
stickerInfo.setCustomSticker(isCustomSticker);
stickerInfo.setCustomImagePath(imageFilePath);
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-112` `deleteCurStickerTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1729`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `get()`, `size()`, `deleteSelectedTimeSpan()`, `remove()`

Simple sequence:

```java
private void deleteCurStickerTimeSpan(NvsTimelineAnimatedSticker animateSticker) {
```

## `captions-stickers-113` `addTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1748`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnTrimInChangeListener`, `NvsTimelineTimeSpan.OnTrimOutChangeListener`
Common calls: `getKeyFrameInfoHashMap()`, `removeAllKeyframe()`, `setKeyFrameInfo()`, `entrySet()`, `getKey()`, `setOnChangeListener()`, `isEmpty()`, `changeStickerRectVisible()`, `getZValue()`, `get()`, `getInPoint()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
private NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");
final NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);
timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {
if (currentStickerInfo != null) {
boolean noInfo = currentStickerInfo.getKeyFrameInfoHashMap().isEmpty();
if (!noInfo) {
mVideoFragment.changeStickerRectVisible();
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentStickerInfo != null && mCurrentStatusIsKeyFrame) {
currentTimeSpan.setKeyFrameInfo(currentStickerInfo.getKeyFrameInfoHashMap());
if (isDragEnd && mCurSelectAnimatedSticker != null) {
mCurSelectAnimatedSticker.changeInPoint(timeStamp);
int zVal = (int) mCurSelectAnimatedSticker.getZValue();
if (index >= 0) {
mStickerDataListClone.get(index).setInPoint(mCurSelectAnimatedSticker.getInPoint());
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = currentStickerInfo.getKeyFrameInfoHashMap();
long currentTimeLinePosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
if (next.getKey() < currentTimeLinePosition) {
if (mCurrentStatusIsKeyFrame) {
currentTimeSpan.setKeyFrameInfo(currentStickerInfo.getKeyFrameInfoHashMap());
boolean removeStickerTransXSuccess = mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransX");
boolean removeStickerTransYSuccess = mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransY");
boolean removeStickerScale = mCurSelectAnimatedSticker.removeAllKeyframe("Sticker Scale");
// ... 24 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-114` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1901`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timestamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER | flag);
```

## `captions-stickers-115` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1909`

API classes: `NvsTimelineAnimatedSticker`, `NvsTimelineTimeSpan`
Common calls: `getFirstAnimatedSticker()`, `getInPoint()`, `getOutPoint()`, `AnimateStickerTimeSpanInfo()`, `add()`, `getNextAnimatedSticker()`

Simple sequence:

```java
NvsTimelineAnimatedSticker animatedSticker = mTimeline.getFirstAnimatedSticker();
while (animatedSticker != null) {
long inPoint = animatedSticker.getInPoint();
long outPoint = animatedSticker.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
animatedSticker = mTimeline.getNextAnimatedSticker(animatedSticker);
```

## `captions-stickers-116` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1911`

API classes: `NvsTimelineTimeSpan`
Common calls: `getInPoint()`, `getOutPoint()`, `AnimateStickerTimeSpanInfo()`, `add()`, `getNextAnimatedSticker()`

Simple sequence:

```java
while (animatedSticker != null) {
long inPoint = animatedSticker.getInPoint();
long outPoint = animatedSticker.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
animatedSticker = mTimeline.getNextAnimatedSticker(animatedSticker);
```

## `captions-stickers-117` `selectAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:1927`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `size()`, `get()`, `getZValue()`, `getTimelineCurrentPosition()`, `getAnimatedStickersByTimelinePosition()`, `e()`

Simple sequence:

```java
if (null == mTimeline) {
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineAnimatedSticker> animateStickerList = mTimeline.getAnimatedStickersByTimelinePosition(curPos);
if (stickerCount > 0) {
float zVal = animateStickerList.get(0).getZValue();
for (int i = 0; i < animateStickerList.size(); i++) {
float tmpZVal = animateStickerList.get(i).getZValue();
```

## `captions-stickers-118` `initMultiSequence`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerActivity.java:2039`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getDuration()`, `getLayoutParams()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();
for (int index = 0; index < clipCount; ++index) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
sequenceDescs.mediaFilePath = videoClip.getFilePath();
sequenceDescs.trimIn = videoClip.getTrimIn();
sequenceDescs.trimOut = videoClip.getTrimOut();
sequenceDescs.inPoint = videoClip.getInPoint();
sequenceDescs.outPoint = videoClip.getOutPoint();
long duration = mTimeline.getDuration();
LinearLayout.LayoutParams layoutParams = (LinearLayout.LayoutParams) mVideoPlay.getLayoutParams();
int halfScreenWidth = ScreenUtils.getScreenWidth(this) / 2;
mTimelineEditor.setSequencLeftPadding(sequenceLeftPadding);
mTimelineEditor.setSequencRightPadding(halfScreenWidth);
mTimelineEditor.setTimeSpanLeftPadding(sequenceLeftPadding);
```

## `captions-stickers-119` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:408`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `captions-stickers-120` `playbackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:413`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`, `changeStickerRectVisible()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
mVideoFragment.changeStickerRectVisible();
```

## `captions-stickers-121` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:414`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`, `changeStickerRectVisible()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
mVideoFragment.changeStickerRectVisible();
```

## `captions-stickers-122` `selectSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/AnimatedStickerAnimationActivity.java:471`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `get()`, `instance()`, `getCurSeekTimelinePos()`, `getAnimatedStickersByTimelinePosition()`, `size()`, `getZValue()`

Simple sequence:

```java
long curPos = BackupData.instance().getCurSeekTimelinePos();
List<NvsTimelineAnimatedSticker> animatedStickers = mTimeline.getAnimatedStickersByTimelinePosition(curPos);
for (int index = 0; index < captionCount; index++) {
int tmpZVal = (int) animatedStickers.get(index).getZValue();
```

## `captions-stickers-123` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerActivity.java:123`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
mStreamingContext = NvsStreamingContext.getInstance();
```

## `captions-stickers-124` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:110`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`

Simple sequence:

```java
mStreamingContext = NvsStreamingContext.getInstance();
```

## `captions-stickers-125` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:159`

API classes: `NvsTimeline`
Common calls: `setVideoFragmentCallBack()`, `VideoFragmentListener()`, `sendEmptyMessage()`

Simple sequence:

```java
mClipFragment.setVideoFragmentCallBack(new SingleClipFragment.VideoFragmentListener() {
public void playBackEOF(NvsTimeline timeline) {
public void playStopped(NvsTimeline timeline) {
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `captions-stickers-126` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:166`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-127` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:171`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `captions-stickers-128` `setCustomStickerImageSize`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/animatesticker/customsticker/CustomAnimateStickerEffectActivity.java:285`

API classes: `NvsAVFileInfo`, `NvsSize`
Common calls: `getLayoutParams()`, `floor()`, `getStatusBarHeight()`, `getScreenWidth()`, `getScreenHeight()`, `getAVFileInfo()`, `getVideoStreamDimension()`, `setLayoutParams()`

Simple sequence:

```java
int statusHeight = ScreenUtils.getStatusBarHeight(this);
int screenWidth = ScreenUtils.getScreenWidth(this);
int screenHeight = ScreenUtils.getScreenHeight(this);
int titleHeight = mTitleBar.getLayoutParams().height;
int bottomHeight = mBottomLayout.getLayoutParams().height;
NvsAVFileInfo avFileInfo = mStreamingContext.getAVFileInfo(imagePath);
if (avFileInfo != null) {
ViewGroup.LayoutParams layoutParams = mCustomStickerIamge.getLayoutParams();
NvsSize videoSize = avFileInfo.getVideoStreamDimension(0);
mCustomStickerIamge.setLayoutParams(layoutParams);
```

## `captions-stickers-129` `initCaptionColorList`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/background/view/MultiColorView.java:86`

API classes: `NvsColor`
Common calls: `setColorValue()`, `nvsColorToHexString()`, `add()`

Simple sequence:

```java
for (MultiColorInfo colorInfo : colorList) {
colorInfo.setColorValue(ColorUtil.nvsColorToHexString(new NvsColor(colorInfo.r, colorInfo.g, colorInfo.b, 1.0F)));
```

## `captions-stickers-130` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:413`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setTimelineScaleForSeek()`, `getDurationWidth()`, `getInstance()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (action == MotionEvent.ACTION_DOWN) {
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-131` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:430`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-132` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:452`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `get()`, `setIsStickerInPlay()`, `size()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoPlay.setBackgroundResource(R.mipmap.icon_edit_pause);
mAssetFragmentsArray.get(mCurTabPage).setIsStickerInPlay(true);
mVideoPlay.setBackgroundResource(R.mipmap.icon_edit_play);
for (int index = 0; index < tapCount; ++index) {
mAssetFragmentsArray.get(index).setIsStickerInPlay(false);
```

## `captions-stickers-133` `updateAllStickerPos`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:643`

API classes: `NvsClipAnimatedSticker`
Static/constants: `NvsClipAnimatedSticker.getInPoint`, `NvsClipAnimatedSticker.removeKeyframeAtTime`, `NvsClipAnimatedSticker.getZValue`, `NvsClipAnimatedSticker.setCurrentKeyFrameTime`
Common calls: `getInPoint()`, `removeKeyframeAtTime()`, `getTimelineCurrentPosition()`, `getAnimatedStickersByClipTimePosition()`, `getZValue()`, `get()`, `getKeyFrameInfoHashMap()`, `isEmpty()`, `setCurrentKeyFrameTime()`, `keySet()`, `contains()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsClipAnimatedSticker> animateStickerList = curVideoClip.getAnimatedStickersByClipTimePosition(curPos);
for (NvsClipAnimatedSticker NvsClipAnimatedSticker : animateStickerList) {
int zVal = (int) NvsClipAnimatedSticker.getZValue();
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = stickerInfo.getKeyFrameInfoHashMap();
NvsClipAnimatedSticker.setCurrentKeyFrameTime(curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker TransX", curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker TransY", curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker Scale", curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker RotZ", curPos - NvsClipAnimatedSticker.getInPoint());
```

## `captions-stickers-134` `updateAllStickerPos`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:646`

API classes: `NvsClipAnimatedSticker`
Static/constants: `NvsClipAnimatedSticker.getInPoint`, `NvsClipAnimatedSticker.removeKeyframeAtTime`, `NvsClipAnimatedSticker.getZValue`, `NvsClipAnimatedSticker.setCurrentKeyFrameTime`
Common calls: `getInPoint()`, `removeKeyframeAtTime()`, `getZValue()`, `get()`, `getKeyFrameInfoHashMap()`, `isEmpty()`, `setCurrentKeyFrameTime()`, `keySet()`, `contains()`

Simple sequence:

```java
for (NvsClipAnimatedSticker NvsClipAnimatedSticker : animateStickerList) {
int zVal = (int) NvsClipAnimatedSticker.getZValue();
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = stickerInfo.getKeyFrameInfoHashMap();
NvsClipAnimatedSticker.setCurrentKeyFrameTime(curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker TransX", curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker TransY", curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker Scale", curPos - NvsClipAnimatedSticker.getInPoint());
NvsClipAnimatedSticker.removeKeyframeAtTime("Sticker RotZ", curPos - NvsClipAnimatedSticker.getInPoint());
```

## `captions-stickers-135` `updateAllKeyFrameViewStatusWhenScroll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:710`

API classes: `NvsTimelineTimeSpan`
Common calls: `setEnabled()`, `getKey()`, `isEmpty()`, `entrySet()`, `keySet()`, `toArray()`, `setCurrentTimelinePosition()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (beforeKeyFrame == -1 || ((objects != null) && ((long) (objects[0]) == timeStamp))) {
mBeforeKeyFrameView.setEnabled(false);
mBeforeKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1 || ((objects != null) && ((long) (objects[objects.length - 1]) == timeStamp))) {
mNextKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
if (timeStamp >= entry.getKey() - 100000 && timeStamp <= entry.getKey() + 100000) {
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentTimeSpan != null) {
currentTimeSpan.setCurrentTimelinePosition(timeStamp);
mBeforeKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(false);
```

## `captions-stickers-136` `updateAllKeyFrameViewStatusWhenScroll`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:712`

API classes: `NvsTimelineTimeSpan`
Common calls: `setEnabled()`, `getKey()`, `entrySet()`, `keySet()`, `toArray()`, `setCurrentTimelinePosition()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (beforeKeyFrame == -1 || ((objects != null) && ((long) (objects[0]) == timeStamp))) {
mBeforeKeyFrameView.setEnabled(false);
mBeforeKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1 || ((objects != null) && ((long) (objects[objects.length - 1]) == timeStamp))) {
mNextKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(true);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
if (timeStamp >= entry.getKey() - 100000 && timeStamp <= entry.getKey() + 100000) {
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentTimeSpan != null) {
currentTimeSpan.setCurrentTimelinePosition(timeStamp);
mBeforeKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(false);
```

## `captions-stickers-137` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:802`

API classes: `NvsTimelineTimeSpan`
Common calls: `setVisibility()`, `getTimelineCurrentPosition()`, `getKeyFrameInfoHashMap()`, `getInPoint()`, `stopEngine()`, `setKeyFrameInfo()`, `setDrawRectVisible()`, `setEnabled()`, `removeAllKeyframe()`, `removeKeyframeAtTime()`, `d()`, `setCurrentKeyFrameTime()`

Simple sequence:

```java
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = currentStickerInfo.getKeyFrameInfoHashMap();
long currentTimelinePosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1) {
mNextKeyFrameView.setEnabled(false);
mNextKeyFrameView.setEnabled(true);
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = currentStickerInfo.getKeyFrameInfoHashMap();
long currentTimelinePosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
Long key = entry.getKey();
if (nextKeyFrame == -1) {
mBeforeKeyFrameView.setEnabled(false);
mBeforeKeyFrameView.setEnabled(true);
if (mCurSelectAnimatedSticker != null) {
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransX");
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransY");
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker Scale");
mCurSelectAnimatedSticker.removeAllKeyframe("Sticker RotZ");
stickerRemoveAllFrameView.setVisibility(View.GONE);
removeFirst.setVisibility(View.GONE);
currentStickerInfo.getKeyFrameInfoHashMap().clear();
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentTimeSpan != null) {
// ... 66 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-138` `selectAnimateStickerByZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1184`

API classes: `NvsClipAnimatedSticker`
Common calls: `size()`, `get()`, `getTimelineCurrentPosition()`, `getAnimatedStickersByClipTimePosition()`, `getZValue()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsClipAnimatedSticker> animateStickerList = curVideoClip.getAnimatedStickersByClipTimePosition(curPos);
for (int i = 0; i < animateStickerList.size(); i++) {
int tmpZVal = (int) animateStickerList.get(i).getZValue();
```

## `captions-stickers-139` `applyAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1451`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `get()`, `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`, `addAnimatedSticker()`, `setZValue()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
mAddAnimateSticker.setZValue(zStickerVal);
```

## `captions-stickers-140` `applyAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1454`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-141` `applyAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1456`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-142` `applyCustomAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1495`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `get()`, `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`, `lastIndexOf()`, `substring()`, `toLowerCase()`, `equals()`, `exists()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-143` `applyCustomAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1498`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-144` `applyCustomAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1500`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-145` `addTimeSpanAndPlayVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1596`

API classes: `NvsTimelineTimeSpan`
Common calls: `get()`, `add()`, `setSelectedPos()`, `notifyDataSetChanged()`, `AnimateStickerTimeSpanInfo()`, `setCustomSticker()`, `setCustomImagePath()`, `setDrawRectVisible()`, `playVideo()`

Simple sequence:

```java
if (mPrevTabPage != mCurTabPage) {
mAssetFragmentsArray.get(mPrevTabPage).setSelectedPos(-1);
NvsTimelineTimeSpan timeSpan = addTimeSpan(mInPoint, endTime);
stickerInfo.setCustomSticker(isCustomSticker);
stickerInfo.setCustomImagePath(imageFilePath);
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-146` `deleteCurStickerTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1729`

API classes: `NvsClipAnimatedSticker`
Common calls: `get()`, `size()`, `deleteSelectedTimeSpan()`, `remove()`

Simple sequence:

```java
private void deleteCurStickerTimeSpan(NvsClipAnimatedSticker animateSticker) {
```

## `captions-stickers-147` `addTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1748`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnTrimInChangeListener`, `NvsTimelineTimeSpan.OnTrimOutChangeListener`
Common calls: `getKeyFrameInfoHashMap()`, `removeAllKeyframe()`, `setKeyFrameInfo()`, `entrySet()`, `getKey()`, `setOnChangeListener()`, `isEmpty()`, `changeStickerRectVisible()`, `getZValue()`, `get()`, `getInPoint()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
private NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");
final NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);
timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {
if (currentStickerInfo != null) {
boolean noInfo = currentStickerInfo.getKeyFrameInfoHashMap().isEmpty();
if (!noInfo) {
mVideoFragment.changeStickerRectVisible();
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentStickerInfo != null && mCurrentStatusIsKeyFrame) {
currentTimeSpan.setKeyFrameInfo(currentStickerInfo.getKeyFrameInfoHashMap());
if (isDragEnd && mCurSelectAnimatedSticker != null) {
mCurSelectAnimatedSticker.changeInPoint(timeStamp);
int zVal = (int) mCurSelectAnimatedSticker.getZValue();
if (index >= 0) {
mStickerDataListClone.get(index).setInPoint(mCurSelectAnimatedSticker.getInPoint());
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = currentStickerInfo.getKeyFrameInfoHashMap();
long currentTimeLinePosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
if (next.getKey() < currentTimeLinePosition) {
if (mCurrentStatusIsKeyFrame) {
currentTimeSpan.setKeyFrameInfo(currentStickerInfo.getKeyFrameInfoHashMap());
boolean removeStickerTransXSuccess = mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransX");
boolean removeStickerTransYSuccess = mCurSelectAnimatedSticker.removeAllKeyframe("Sticker TransY");
boolean removeStickerScale = mCurSelectAnimatedSticker.removeAllKeyframe("Sticker Scale");
// ... 24 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-148` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1897`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timestamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-149` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1905`

API classes: `NvsClipAnimatedSticker`, `NvsTimelineTimeSpan`
Common calls: `getFirstAnimatedSticker()`, `getInPoint()`, `getOutPoint()`, `AnimateStickerTimeSpanInfo()`, `add()`, `getNextAnimatedSticker()`

Simple sequence:

```java
NvsClipAnimatedSticker animatedSticker = curVideoClip.getFirstAnimatedSticker();
while (animatedSticker != null) {
long inPoint = animatedSticker.getInPoint();
long outPoint = animatedSticker.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
animatedSticker = curVideoClip.getNextAnimatedSticker(animatedSticker);
```

## `captions-stickers-150` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1907`

API classes: `NvsTimelineTimeSpan`
Common calls: `getInPoint()`, `getOutPoint()`, `AnimateStickerTimeSpanInfo()`, `add()`, `getNextAnimatedSticker()`

Simple sequence:

```java
while (animatedSticker != null) {
long inPoint = animatedSticker.getInPoint();
long outPoint = animatedSticker.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
animatedSticker = curVideoClip.getNextAnimatedSticker(animatedSticker);
```

## `captions-stickers-151` `selectAnimateSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:1923`

API classes: `NvsClipAnimatedSticker`
Common calls: `size()`, `get()`, `getZValue()`, `getTimelineCurrentPosition()`, `getAnimatedStickersByClipTimePosition()`, `e()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsClipAnimatedSticker> animateStickerList = curVideoClip.getAnimatedStickersByClipTimePosition(curPos);
if (stickerCount > 0) {
float zVal = animateStickerList.get(0).getZValue();
for (int i = 0; i < animateStickerList.size(); i++) {
float tmpZVal = animateStickerList.get(i).getZValue();
```

## `captions-stickers-152` `initMultiSequence`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerActivity.java:2032`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getDuration()`, `getLayoutParams()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();
for (int index = 0; index < clipCount; ++index) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
sequenceDescs.mediaFilePath = videoClip.getFilePath();
sequenceDescs.trimIn = videoClip.getTrimIn();
sequenceDescs.trimOut = videoClip.getTrimOut();
sequenceDescs.inPoint = videoClip.getInPoint();
sequenceDescs.outPoint = videoClip.getOutPoint();
long duration = mTimeline.getDuration();
LinearLayout.LayoutParams layoutParams = (LinearLayout.LayoutParams) mVideoPlay.getLayoutParams();
int halfScreenWidth = ScreenUtils.getScreenWidth(this) / 2;
mTimelineEditor.setSequencLeftPadding(sequenceLeftPadding);
mTimelineEditor.setSequencRightPadding(halfScreenWidth);
mTimelineEditor.setTimeSpanLeftPadding(sequenceLeftPadding);
```

## `captions-stickers-153` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:426`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
```

## `captions-stickers-154` `playbackTimelinePosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:431`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`, `changeStickerRectVisible()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
mVideoFragment.changeStickerRectVisible();
```

## `captions-stickers-155` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:432`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setDrawRectVisible()`, `changeStickerRectVisible()`

Simple sequence:

```java
if (state == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mVideoFragment.setDrawRectVisible(View.GONE);
mVideoFragment.changeStickerRectVisible();
```

## `captions-stickers-156` `selectSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/animatedSticker/ClipAnimatedStickerAnimationActivity.java:489`

API classes: `NvsClipAnimatedSticker`
Common calls: `get()`, `instance()`, `getCurSeekTimelinePos()`, `getAnimatedStickersByClipTimePosition()`, `size()`, `getZValue()`

Simple sequence:

```java
long curPos = BackupData.instance().getCurSeekTimelinePos();
List<NvsClipAnimatedSticker> animatedStickers = curVideoClip.getAnimatedStickersByClipTimePosition(curPos);
for (int index = 0; index < captionCount; index++) {
int tmpZVal = (int) animatedStickers.get(index).getZValue();
```

## `captions-stickers-157` `playbackTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:181`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER | flag);
```

## `captions-stickers-158` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:185`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-159` `initRootView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:234`

API classes: `NvsTimelineEditor`
Common calls: `setMax()`, `getMultiThumbnailSequenceView()`

Simple sequence:

```java
mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.caption_timeline_editor);
alphaSeek.setMax(100);
mMultiSequenceView = mTimelineEditor.getMultiThumbnailSequenceView();
```

## `captions-stickers-160` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:373`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOpacity()`, `getTimelineCurrentPosition()`, `setOnSeekBarChangeListener()`, `setText()`, `getMax()`, `getInPoint()`, `setFloatValAtTime()`, `getStreamingEngineState()`

Simple sequence:

```java
alphaSeek.setOnSeekBarChangeListener(new OnSeekBarChangeListenerAbs() {
if (mCurCaption != null) {
seekBarOpacityWidthValue.setText(i + "");
float opacity = i * 1f / alphaSeek.getMax();
if (currentCaptionInfo != null) {
currentCaptionInfo.setOpacity(opacity);
mCurCaption.setOpacity(opacity);
long duration = mStreamingContext.getTimelineCurrentPosition(mTimeline) - mCurCaption.getInPoint();
mCurCaption.setFloatValAtTime(TRACK_OPACITY, opacity, duration);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-161` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:375`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOpacity()`, `getTimelineCurrentPosition()`, `setText()`, `getMax()`, `getInPoint()`, `setFloatValAtTime()`, `getStreamingEngineState()`

Simple sequence:

```java
if (mCurCaption != null) {
seekBarOpacityWidthValue.setText(i + "");
float opacity = i * 1f / alphaSeek.getMax();
if (currentCaptionInfo != null) {
currentCaptionInfo.setOpacity(opacity);
mCurCaption.setOpacity(opacity);
long duration = mStreamingContext.getTimelineCurrentPosition(mTimeline) - mCurCaption.getInPoint();
mCurCaption.setFloatValAtTime(TRACK_OPACITY, opacity, duration);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-162` `onProgressChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:379`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setOpacity()`, `getTimelineCurrentPosition()`, `setText()`, `getMax()`, `getInPoint()`, `setFloatValAtTime()`, `getStreamingEngineState()`

Simple sequence:

```java
if (mCurCaption != null) {
seekBarOpacityWidthValue.setText(i + "");
float opacity = i * 1f / alphaSeek.getMax();
if (currentCaptionInfo != null) {
currentCaptionInfo.setOpacity(opacity);
mCurCaption.setOpacity(opacity);
long duration = mStreamingContext.getTimelineCurrentPosition(mTimeline) - mCurCaption.getInPoint();
mCurCaption.setFloatValAtTime(TRACK_OPACITY, opacity, duration);
if (mStreamingContext.getStreamingEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-163` `onScrollX`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:421`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getTimelineCurrentPosition()`, `getAction()`, `setDrawRectVisible()`, `unSelectAllTimeSpan()`, `getInstance()`, `getVisibility()`

Simple sequence:

```java
switch (event.getAction()) {
mVideoFragment.setDrawRectVisible(View.GONE);
seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));
if (mLlKeyFrame.getVisibility() == View.VISIBLE) {
updateCaptionRelativeView(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-164` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:423`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getTimelineCurrentPosition()`, `getAction()`, `setDrawRectVisible()`, `unSelectAllTimeSpan()`, `getInstance()`, `getVisibility()`

Simple sequence:

```java
switch (event.getAction()) {
mVideoFragment.setDrawRectVisible(View.GONE);
seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));
if (mLlKeyFrame.getVisibility() == View.VISIBLE) {
updateCaptionRelativeView(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-165` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:452`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-166` `playStopped`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:457`

API classes: `NvsTimeline`
Common calls: `setDrawRectVisible()`, `unSelectAllTimeSpan()`, `round()`, `getDuration()`, `getSequenceWidth()`, `smoothScrollTo()`

Simple sequence:

```java
public void playbackTimelinePosition(NvsTimeline timeline, long stamp) {
mVideoFragment.setDrawRectVisible(View.GONE);
if (mMultiSequenceView != null) {
int x = Math.round((stamp / (float) mTimeline.getDuration() * mTimelineEditor.getSequenceWidth()));
```

## `captions-stickers-167` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:470`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setBackgroundResource()`, `getKeyFrameInfo()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK == state) {
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_pause);
mPlayBtn.setBackgroundResource(R.mipmap.icon_edit_play);
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
updateKeyFrameView(mStreamingContext.getTimelineCurrentPosition(mTimeline), keyFrameInfo);
```

## `captions-stickers-168` `updateCaptionControlPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:793`

API classes: `NvsPointD`, `NvsControlPointPair`
Common calls: `getInPoint()`, `getValue()`, `getControlPoint()`, `setControlPoint()`, `getTranslation()`, `setCurrentKeyFrameTime()`, `setForwardControlPointX()`, `setForwardControlPointYForTransX()`, `setForwardControlPointYForTransY()`, `setBackwardControlPointX()`, `setBackwardControlPointYForTransX()`, `setBackwardControlPointYForTransY()`

Simple sequence:

```java
PointF beforePointF = mBeforeKeyMapInfo.getValue().getTranslation();
PointF nextPointF = mNextKeyMapInfo.getValue().getTranslation();
mCurCaption.setCurrentKeyFrameTime(beforeTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (pairY == null) {
pairY = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairY.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransY);
mCurCaption.setControlPoint(TRANS_Y, pairY);
KeyFrameInfo keyFrameInfo = mBeforeKeyMapInfo.getValue();
keyFrameInfo.setForwardControlPointX(forwardControlPointX);
keyFrameInfo.setForwardControlPointYForTransX(forwardControlPointYForTransX);
keyFrameInfo.setForwardControlPointYForTransY(forwardControlPointYForTransY);
mCurCaption.setCurrentKeyFrameTime(nextTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.backwardControlPoint = new NvsPointD(backwardControlPointX - mCurCaption.getInPoint(), backwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
// ... 8 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-169` `updateCaptionControlPoint`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:796`

API classes: `NvsPointD`, `NvsControlPointPair`
Common calls: `getInPoint()`, `getControlPoint()`, `setControlPoint()`, `setCurrentKeyFrameTime()`, `getValue()`, `setForwardControlPointX()`, `setForwardControlPointYForTransX()`, `setForwardControlPointYForTransY()`, `setBackwardControlPointX()`, `setBackwardControlPointYForTransX()`, `setBackwardControlPointYForTransY()`

Simple sequence:

```java
mCurCaption.setCurrentKeyFrameTime(beforeTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (pairY == null) {
pairY = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairY.forwardControlPoint = new NvsPointD(forwardControlPointX - mCurCaption.getInPoint(), forwardControlPointYForTransY);
mCurCaption.setControlPoint(TRANS_Y, pairY);
KeyFrameInfo keyFrameInfo = mBeforeKeyMapInfo.getValue();
keyFrameInfo.setForwardControlPointX(forwardControlPointX);
keyFrameInfo.setForwardControlPointYForTransX(forwardControlPointYForTransX);
keyFrameInfo.setForwardControlPointYForTransY(forwardControlPointYForTransY);
mCurCaption.setCurrentKeyFrameTime(nextTimeStamp - mCurCaption.getInPoint());
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
if (pairX == null) {
pairX = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
pairX.backwardControlPoint = new NvsPointD(backwardControlPointX - mCurCaption.getInPoint(), backwardControlPointYForTransX);
mCurCaption.setControlPoint(TRANS_X, pairX);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (pairY == null) {
pairY = new NvsControlPointPair(new NvsPointD(0, 0), new NvsPointD(0, 0));
// ... 6 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-170` `updateCaptionRelativeView`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:848`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`
Common calls: `getInPoint()`, `getKey()`, `getZValue()`, `getKeyFrameInfo()`, `getTimelineCurrentPosition()`, `getFloatValAtTime()`, `setProgress()`, `getMax()`, `getOutPoint()`, `setDrawRectVisible()`, `entrySet()`, `setCurrentKeyFrameTime()`

Simple sequence:

```java
if (mCurCaption != null) {
captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
keyFrameMap = captionInfo.getKeyFrameInfo();
long currentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
&& (currentPosition - mCurCaption.getInPoint() >= minTime)
&& (currentPosition - mCurCaption.getInPoint() <= maxTime)) {
double floatValAtTime = mCurCaption.getFloatValAtTime(TRACK_OPACITY, currentPosition - mCurCaption.getInPoint());
alphaSeek.setProgress((int) ((floatValAtTime) * alphaSeek.getMax()));
if (mCurCaption != null) {
if (timeStamp > mCurCaption.getOutPoint() + 1000 || timeStamp < mCurCaption.getInPoint() - 1000) {
mVideoFragment.setDrawRectVisible(View.GONE);
for (Map.Entry<Long, KeyFrameInfo> entry : keyFrameMap.entrySet()) {
if (timeStamp >= entry.getKey() - 100000 && timeStamp <= entry.getKey() + 100000) {
currentKeyFrameStamp = entry.getKey();
if (hasKeyFrame) {
mCurCaption.setCurrentKeyFrameTime(currentKeyFrameStamp - mCurCaption.getInPoint());
mTvAddDeleteFrame.setEnabled(true);
if (mTimeline != null) {
seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `captions-stickers-171` `generateKeyFrameInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1135`

API classes: `NvsClipCaption`
Common calls: `setScaleX()`, `getScaleX()`, `setScaleY()`, `getScaleY()`, `setRotationZ()`, `getRotationZ()`, `setTranslation()`, `getCaptionTranslation()`, `setOpacity()`, `getOpacity()`

Simple sequence:

```java
private KeyFrameInfo generateKeyFrameInfo(NvsClipCaption caption) {
return new KeyFrameInfo().setScaleX(caption.getScaleX())
.setScaleY(caption.getScaleY())
.setRotationZ(caption.getRotationZ())
.setTranslation(caption.getCaptionTranslation())
.setOpacity(caption.getOpacity());
```

## `captions-stickers-172` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1146`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `setVisibility()`, `instance()`, `getInstance()`, `getDuration()`, `showToastCenter()`, `getString()`, `OnCloseListener()`, `getUserInputText()`, `show()`, `getKeyFrameInfo()`, `setKeyFrameInfo()`, `stop()`

Simple sequence:

```java
mCaptionStyleButton.setClickable(false);
if (currentCaptionInfo1 != null) {
currentCaptionInfo1.setTranslation(mCurCaption.getCaptionTranslation());
currentCaptionInfo1.setScaleFactorX(mCurCaption.getScaleX());
currentCaptionInfo1.setScaleFactorY(mCurCaption.getScaleY());
currentCaptionInfo1.setRotation(mCurCaption.getRotationZ());
BackupData.instance().setClipCaptionList(mCaptionDataListClone);
BackupData.instance().setCaptionZVal((int) mCurCaption.getZValue());
BackupData.instance().setCurSeekTimelinePos(mCurCaption.getInPoint());
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), ClipCaptionStyleActivity.class, bundle, REQUESTCAPTIONSTYLE);
if (mTimeline.getDuration() < NS_TIME_BASE) {
ToastUtil.showToastCenter(getApplicationContext(), getResources().getString(R.string.tips_add_caption_restrictions));
String userInputText = d.getUserInputText();
if (mTimeline.getDuration() < NS_TIME_BASE) {
ToastUtil.showToastCenter(getApplicationContext(), getResources().getString(R.string.tips_add_caption_restrictions));
String userInputText = d.getUserInputText();
if (mLlKeyFrame.getVisibility() == View.VISIBLE) {
Map<Long, KeyFrameInfo> keyFrameInfo = currentCaptionInfo.getKeyFrameInfo();
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
mCaptionStyleButton.setVisibility(View.VISIBLE);
mStreamingContext.stop();
BackupData.instance().setClipInfoData(mClipArrayList);
AppManager.getInstance().finishActivity();
// ... 14 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-173` `selectCaptionByZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1572`

API classes: `NvsClipCaption`
Common calls: `get()`, `getZValue()`, `setVisibility()`, `getTimelineCurrentPosition()`, `getCaptionsByClipTimePosition()`, `size()`, `getKeyFrameInfo()`, `isEmpty()`

Simple sequence:

```java
if (mTimeline != null) {
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsClipCaption> captionList = curVideoClip.getCaptionsByClipTimePosition(curPos);
for (int i = 0; i < captionCount; i++) {
int zVal = (int) captionList.get(i).getZValue();
if (mCurCaption != null) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
mCaptionStyleButton.setVisibility(View.GONE);
```

## `captions-stickers-174` `selectCaptionByZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1573`

API classes: `NvsClipCaption`
Common calls: `get()`, `getZValue()`, `setVisibility()`, `getTimelineCurrentPosition()`, `getCaptionsByClipTimePosition()`, `size()`, `getKeyFrameInfo()`, `isEmpty()`

Simple sequence:

```java
if (mTimeline != null) {
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsClipCaption> captionList = curVideoClip.getCaptionsByClipTimePosition(curPos);
for (int i = 0; i < captionCount; i++) {
int zVal = (int) captionList.get(i).getZValue();
if (mCurCaption != null) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
mCaptionStyleButton.setVisibility(View.GONE);
```

## `captions-stickers-175` `playVideo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1602`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getTimelineCurrentPosition()`, `getDuration()`, `playVideo()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
long startTime = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long endTime = mTimeline.getDuration();
```

## `captions-stickers-176` `getCurCaptionZVal`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1629`

API classes: `NvsClipCaption`
Common calls: `getFirstCaption()`, `getZValue()`, `getNextCaption()`

Simple sequence:

```java
NvsClipCaption caption = curVideoClip.getFirstCaption();
while (caption != null) {
float tmpZVal = caption.getZValue();
caption = curVideoClip.getNextCaption(caption);
```

## `captions-stickers-177` `addCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1730`

API classes: `NvsTimelineTimeSpan`
Common calls: `e()`, `add()`, `getOpacity()`, `getMax()`, `getTimelineCurrentPosition()`, `getDuration()`, `addCaption()`, `addModularCaption()`, `setZValue()`, `setVisibility()`, `setTraditional()`, `getTimeSpanshadowView()`

Simple sequence:

```java
long inPoint = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long duration = mTimeline.getDuration();
mCurCaption.setZValue(zVal);
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
mCaptionStyleButton.setVisibility(View.VISIBLE);
info.setTraditional(traditional);
if (!traditional) {
timeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
mVideoFragment.setCurCaption(mCurCaption);
int alignVal = mCurCaption.getTextAlignment();
mVideoFragment.setAlignIndex(alignVal);
mVideoFragment.changeCaptionRectVisible();
if (captionInfo != null) {
captionInfo.setTraditionCaption(traditional);
if (mCurCaption != null) {
alphaSeek.setProgress((int) (mCurCaption.getOpacity() * alphaSeek.getMax()));
seekBarOpacityWidthValue.setText((int) (mCurCaption.getOpacity() * alphaSeek.getMax()) + "");
```

## `captions-stickers-178` `addTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1803`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnTrimInChangeListener`, `NvsTimelineTimeSpan.OnTrimOutChangeListener`
Common calls: `getKey()`, `getKeyFrameInfo()`, `entrySet()`, `getTimelineCurrentPosition()`, `getInPoint()`, `setOnChangeListener()`, `changeCaptionRectVisible()`, `getZValue()`, `get()`, `isEmpty()`, `iterator()`, `hasNext()`

Simple sequence:

```java
private NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");
NvsTimelineTimeSpan timelineTimeSpan = mTimelineEditor.addTimeSpan(inPoint, outPoint);
timelineTimeSpan.setOnChangeListener(new NvsTimelineTimeSpan.OnTrimInChangeListener() {
mVideoFragment.changeCaptionRectVisible();
NvsTimelineTimeSpan currentTimeSpan = getCurrentTimeSpan();
if (currentCaptionInfo != null && mAddKeyFrame) {
currentTimeSpan.setKeyFrameInfo(currentCaptionInfo.getKeyFrameInfo());
if (mCurCaption != null) {
mCurCaption.changeInPoint(timeStamp);
int zVal = (int) mCurCaption.getZValue();
if (index >= 0) {
mCaptionDataListClone.get(index).setInPoint(timeStamp);
mVideoFragment.setDrawRectVisible(View.GONE);
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = captionInfo.getKeyFrameInfo();
long currentPosition = mStreamingContext.getTimelineCurrentPosition(mTimeline);
Log.d(TAG, " trimIn:" + timeStamp + " itemKey:" + next.getKey() + " timelinePosition:" + currentPosition);
if (next.getKey() < currentPosition) {
removeKeyFrameByCurrentTime(next.getKey());
Map<Long, KeyFrameInfo> keyFrameInfoHashMapAfter = captionInfo.getKeyFrameInfo();
for (Map.Entry<Long, KeyFrameInfo> longCaptionKeyFrameInfoEntry : entriesAfter) {
KeyFrameInfo captionKeyFrameInfo = longCaptionKeyFrameInfoEntry.getValue();
addKeyFrameOnCurrentTime(longCaptionKeyFrameInfoEntry.getKey() - mCurCaption.getInPoint(),
// ... 25 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-179` `rebuildBezierData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1970`

API classes: `NvsControlPointPair`
Common calls: `getInPoint()`, `getControlPoint()`, `setControlPoint()`, `getValue()`, `getForwardControlPointX()`, `getBackwardControlPointX()`, `getKey()`, `setCurrentKeyFrameTime()`, `getBackwardControlPointYForTransX()`, `getBackwardControlPointYForTransY()`, `getForwardControlPointYForTransX()`, `getForwardControlPointYForTransY()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> longCaptionKeyFrameInfoEntry : entriesAfter) {
KeyFrameInfo keyFrameInfo = longCaptionKeyFrameInfoEntry.getValue();
double forwardControlPointX = keyFrameInfo.getForwardControlPointX();
double backwardControlPointX = keyFrameInfo.getBackwardControlPointX();
long duration = longCaptionKeyFrameInfoEntry.getKey() - mCurCaption.getInPoint();
mCurCaption.setCurrentKeyFrameTime(duration);
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (backwardControlPointX != -1) {
pairX.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairX.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransX();
pairY.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairY.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransY();
if (forwardControlPointX != -1) {
pairX.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairX.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransX();
pairY.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairY.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransY();
mCurCaption.setControlPoint(TRANS_X, pairX);
mCurCaption.setControlPoint(TRANS_Y, pairY);
```

## `captions-stickers-180` `rebuildBezierData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:1973`

API classes: `NvsControlPointPair`
Common calls: `getInPoint()`, `getControlPoint()`, `setControlPoint()`, `getValue()`, `getForwardControlPointX()`, `getBackwardControlPointX()`, `getKey()`, `setCurrentKeyFrameTime()`, `getBackwardControlPointYForTransX()`, `getBackwardControlPointYForTransY()`, `getForwardControlPointYForTransX()`, `getForwardControlPointYForTransY()`

Simple sequence:

```java
for (Map.Entry<Long, KeyFrameInfo> longCaptionKeyFrameInfoEntry : entriesAfter) {
KeyFrameInfo keyFrameInfo = longCaptionKeyFrameInfoEntry.getValue();
double forwardControlPointX = keyFrameInfo.getForwardControlPointX();
double backwardControlPointX = keyFrameInfo.getBackwardControlPointX();
long duration = longCaptionKeyFrameInfoEntry.getKey() - mCurCaption.getInPoint();
mCurCaption.setCurrentKeyFrameTime(duration);
NvsControlPointPair pairX = mCurCaption.getControlPoint(TRANS_X);
NvsControlPointPair pairY = mCurCaption.getControlPoint(TRANS_Y);
if (backwardControlPointX != -1) {
pairX.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairX.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransX();
pairY.backwardControlPoint.x = backwardControlPointX - mCurCaption.getInPoint();
pairY.backwardControlPoint.y = keyFrameInfo.getBackwardControlPointYForTransY();
if (forwardControlPointX != -1) {
pairX.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairX.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransX();
pairY.forwardControlPoint.x = forwardControlPointX - mCurCaption.getInPoint();
pairY.forwardControlPoint.y = keyFrameInfo.getForwardControlPointYForTransY();
mCurCaption.setControlPoint(TRANS_X, pairX);
mCurCaption.setControlPoint(TRANS_Y, pairY);
```

## `captions-stickers-181` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2114`

API classes: `NvsClipCaption`, `NvsTimelineTimeSpan`
Static/constants: `NvsClipCaption.THEME_CATEGORY`, `NvsClipCaption.ROLE_IN_THEME_GENERAL`
Common calls: `isModular()`, `getNextCaption()`, `getFirstCaption()`, `getCategory()`, `getRoleInTheme()`, `e()`, `getInPoint()`, `getOutPoint()`, `setTraditional()`, `getTimeSpanshadowView()`, `setBackgroundColor()`, `getColor()`

Simple sequence:

```java
NvsClipCaption caption = curVideoClip.getFirstCaption();
while (caption != null) {
int capCategory = caption.getCategory();
int roleTheme = caption.getRoleInTheme();
if (capCategory == NvsClipCaption.THEME_CATEGORY
&& roleTheme != NvsClipCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作编辑处理 Subject captions are not edited
caption = curVideoClip.getNextCaption(caption);
long inPoint = caption.getInPoint();
long outPoint = caption.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
timeSpanInfo.setTraditional(!caption.isModular());
if (!timeSpanInfo.isTraditional) {
timeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
caption = curVideoClip.getNextCaption(caption);
```

## `captions-stickers-182` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2116`

API classes: `NvsClipCaption`, `NvsTimelineTimeSpan`
Static/constants: `NvsClipCaption.THEME_CATEGORY`, `NvsClipCaption.ROLE_IN_THEME_GENERAL`
Common calls: `isModular()`, `getNextCaption()`, `getCategory()`, `getRoleInTheme()`, `e()`, `getInPoint()`, `getOutPoint()`, `setTraditional()`, `getTimeSpanshadowView()`, `setBackgroundColor()`, `getColor()`, `add()`

Simple sequence:

```java
while (caption != null) {
int capCategory = caption.getCategory();
int roleTheme = caption.getRoleInTheme();
if (capCategory == NvsClipCaption.THEME_CATEGORY
&& roleTheme != NvsClipCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作编辑处理 Subject captions are not edited
caption = curVideoClip.getNextCaption(caption);
long inPoint = caption.getInPoint();
long outPoint = caption.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
timeSpanInfo.setTraditional(!caption.isModular());
if (!timeSpanInfo.isTraditional) {
timeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
caption = curVideoClip.getNextCaption(caption);
```

## `captions-stickers-183` `selectCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2152`

API classes: `NvsClipCaption`
Static/constants: `NvsClipCaption.THEME_CATEGORY`, `NvsClipCaption.ROLE_IN_THEME_GENERAL`
Common calls: `get()`, `getZValue()`, `setKeyFrameInfo()`, `setVisibility()`, `getKeyFrameInfo()`, `getTimelineCurrentPosition()`, `getCaptionsByClipTimePosition()`, `size()`, `getCategory()`, `getRoleInTheme()`, `getVisibility()`, `isEmpty()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsClipCaption> captionList = curVideoClip.getCaptionsByClipTimePosition(curPos);
if (captionCount > 0) {
float zVal = captionList.get(0).getZValue();
for (int i = 0; i < captionCount; i++) {
float tmpZVal = captionList.get(i).getZValue();
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(currentCaptionInfo.getKeyFrameInfo());
if (mCurCaption.getCategory() == NvsClipCaption.THEME_CATEGORY
&& mCurCaption.getRoleInTheme() != NvsClipCaption.ROLE_IN_THEME_GENERAL) {
mCaptionStyleButton.setVisibility(View.GONE);
if (mLlKeyFrame.getVisibility() != View.VISIBLE) {
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
if (!mAddKeyFrame) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
mCaptionStyleButton.setVisibility(View.GONE);
```

## `captions-stickers-184` `selectCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2156`

API classes: `NvsClipCaption`
Static/constants: `NvsClipCaption.THEME_CATEGORY`, `NvsClipCaption.ROLE_IN_THEME_GENERAL`
Common calls: `get()`, `getZValue()`, `setKeyFrameInfo()`, `setVisibility()`, `getKeyFrameInfo()`, `getCategory()`, `getRoleInTheme()`, `getVisibility()`, `isEmpty()`

Simple sequence:

```java
if (captionCount > 0) {
float zVal = captionList.get(0).getZValue();
for (int i = 0; i < captionCount; i++) {
float tmpZVal = captionList.get(i).getZValue();
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(currentCaptionInfo.getKeyFrameInfo());
if (mCurCaption.getCategory() == NvsClipCaption.THEME_CATEGORY
&& mCurCaption.getRoleInTheme() != NvsClipCaption.ROLE_IN_THEME_GENERAL) {
mCaptionStyleButton.setVisibility(View.GONE);
if (mLlKeyFrame.getVisibility() != View.VISIBLE) {
CaptionInfo captionInfo = getCaptionInfo((int) mCurCaption.getZValue());
if (captionInfo != null) {
Map<Long, KeyFrameInfo> keyFrameInfo = captionInfo.getKeyFrameInfo();
if (!mAddKeyFrame) {
mCaptionStyleButton.setVisibility(View.VISIBLE);
if (spanInfo != null && spanInfo.mTimeSpan != null) {
spanInfo.mTimeSpan.setKeyFrameInfo(null);
mCaptionStyleButton.setVisibility(View.GONE);
```

## `captions-stickers-185` `selectTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2226`

API classes: `NvsTimelineTimeSpan`
Common calls: `get()`, `selectTimeSpan()`

Simple sequence:

```java
if (captionTimeSpanInfo.mCaption == mCurCaption) {
NvsTimelineTimeSpan timeSpan = mTimeSpanInfoList.get(i).mTimeSpan;
```

## `captions-stickers-186` `selectTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionActivity.java:2227`

API classes: `NvsTimelineTimeSpan`
Common calls: `get()`, `selectTimeSpan()`

Simple sequence:

```java
if (captionTimeSpanInfo.mCaption == mCurCaption) {
NvsTimelineTimeSpan timeSpan = mTimeSpanInfoList.get(i).mTimeSpan;
```

## `captions-stickers-187` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:558`

API classes: `NvsTimeline`
Common calls: `sendEmptyMessage()`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-188` `updateCaptionPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:916`

API classes: `NvsClipCaption`
Static/constants: `NvsClipCaption.THEME_CATEGORY`, `NvsClipCaption.ROLE_IN_THEME_GENERAL`
Common calls: `get()`, `sort()`, `translateCaption()`, `getNextCaption()`, `getVideoRes()`, `PointXComparator()`, `PointYComparator()`, `getCategory()`, `getRoleInTheme()`, `getZValue()`, `getBoundingRectangleVertices()`, `size()`

Simple sequence:

```java
while (caption != null) {
if (caption.getCategory() == NvsClipCaption.THEME_CATEGORY
&& caption.getRoleInTheme()
!= NvsClipCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作处理 Subject subtitles are not processed
caption = curVideoClip.getNextCaption(caption);
int zVal = (int) caption.getZValue();
if (mCurCaptionZVal == zVal) {
caption = curVideoClip.getNextCaption(caption);
List<PointF> list = caption.getBoundingRectangleVertices();
if (list == null || list.size() < 4) {
caption = curVideoClip.getNextCaption(caption);
float xLeftOffset = -(mTimeline.getVideoRes().imageWidth / 2 + list.get(0).x);
float xRightOffset = mTimeline.getVideoRes().imageWidth / 2 - list.get(3).x;
float yTopOffset = mTimeline.getVideoRes().imageHeight / 2 - list.get(0).y - yTopdis;
-(mTimeline.getVideoRes().imageHeight / 2 + list.get(3).y - yBottomdis);
mCaptionDataListClone.get(index).setTranslation(caption.getCaptionTranslation());
mCaptionDataListClone.get(index).setUsedTranslationFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
caption = curVideoClip.getNextCaption(caption);
```

## `captions-stickers-189` `updateCaptionPosition`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:919`

API classes: `NvsClipCaption`
Static/constants: `NvsClipCaption.ROLE_IN_THEME_GENERAL`
Common calls: `getNextCaption()`

Simple sequence:

```java
!= NvsClipCaption.ROLE_IN_THEME_GENERAL) {//主题字幕不作处理 Subject subtitles are not processed
caption = curVideoClip.getNextCaption(caption);
```

## `captions-stickers-190` `initCaptionStyleFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:1989`

API classes: `NvsColor`
Common calls: `putInt()`, `getInstance()`, `getInPoint()`, `playVideo()`, `get()`, `setCaptionStyleListener()`, `OnCaptionStyleListener()`, `applyToAllCaption()`, `setSelectedPos()`, `notifyDataSetChanged()`, `stopEngine()`, `jumpActivityForResult()`

Simple sequence:

```java
captionStyleFragment.setCaptionStyleListener(new CaptionStyleFragment.OnCaptionStyleListener() {
mCaptionStyleFragment.applyToAllCaption(bIsStyleUuidApplyToAll);
mCaptionStyleFragment.setSelectedPos(mSelectedStylePos);
AppManager.getInstance()
.jumpActivityForResult(AppManager.getInstance().currentActivity(),
long startTime = mCurAddCaption.getInPoint();
long endTime = mCurAddCaption.getOutPoint();
mVideoFragment.setDrawRectVisible(View.GONE);
NvAsset asset = mTotalCaptionStyleList.get(pos).getAsset();
mCurAddCaption.applyCaptionStyle(asset.uuid);
float captionSize = mCurAddCaption.getFontSize();
float scaleX = mCurAddCaption.getScaleX();
float scaleY = mCurAddCaption.getScaleY();
PointF pointF = mCurAddCaption.getCaptionTranslation();
float rotateAngle = mCurAddCaption.getRotationZ();
if (captionInfo != null) {
captionInfo.setCaptionStyleUuid(asset.uuid);
captionInfo.setTranslation(pointF);
captionInfo.setCaptionSize(captionSize);
captionInfo.setScaleFactorX(scaleX);
captionInfo.setScaleFactorY(scaleY);
captionInfo.setRotation(rotateAngle);
captionInfo.setBold(mCurAddCaption.getBold());
if (captionInfo.getUsedColorFlag() == CaptionInfo.ATTRIBUTE_USED_FLAG) {
// ... 4 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-191` `initCaptionColorFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2136`

API classes: `NvsColor`
Common calls: `get()`, `notifyDataSetChanged()`, `updateCaptionOpacityValue()`, `setTextColor()`, `setUsedColorFlag()`, `setCaptionColor()`, `setCaptionColorListener()`, `OnCaptionColorListener()`, `applyToAllCaption()`, `setCaptionColorInfolist()`, `getCaptionColorAlpha()`, `size()`

Simple sequence:

```java
captionColorFragment.setCaptionColorListener(new CaptionColorFragment.OnCaptionColorListener() {
mCaptionColorFragment.applyToAllCaption(bIsCaptionColorApplyToAll);
mCaptionColorFragment.setCaptionColorInfolist(mCaptionColorList);
if (index >= 0) {
mCaptionColorOpacityValue = mCaptionDataListClone.get(index).getCaptionColorAlpha();
NvsColor color = ColorUtil.colorStringtoNvsColor(mCaptionColorList.get(pos).mColorValue);
mCurAddCaption.setTextColor(color);
if (index >= 0) {
mCaptionDataListClone.get(index).setUsedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setCaptionColor(mCaptionColorList.get(pos).mColorValue);
NvsColor curColor = mCurAddCaption.getTextColor();
mCurAddCaption.setTextColor(curColor);
if (index >= 0) {
mCaptionDataListClone.get(index).setUsedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setCaptionColor(strColor);
mCaptionDataListClone.get(index).setCaptionColorAlpha(progress);
```

## `captions-stickers-192` `initCaptionOutlineFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2222`

API classes: `NvsColor`
Common calls: `get()`, `setOutlineColor()`, `setOutlineWidth()`, `notifyDataSetChanged()`, `updateCaptionOutlineWidthValue()`, `updateCaptionOutlineOpacityValue()`, `setDrawOutline()`, `setUsedOutlineFlag()`, `setHasOutline()`, `setOutlineColorAlpha()`, `OnCaptionOutlineListener()`, `applyToAllCaption()`

Simple sequence:

```java
mCaptionOutlineFragment.applyToAllCaption(bIsOutlineApplyToAll);
mCaptionOutlineFragment.setCaptionOutlineInfolist(mCaptionOutlineColorList);
(int) mCaptionDataListClone.get(index).getOutlineWidth();
mCaptionDataListClone.get(index).getOutlineColorAlpha();
if (pos == 0) {
mCurAddCaption.setDrawOutline(false);
.setUsedOutlineFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setHasOutline(false);
mCaptionDataListClone.get(index).setOutlineColor("");
mCurAddCaption.setDrawOutline(true);
NvsColor color =
mCurAddCaption.setOutlineColor(color);
mCurAddCaption.setOutlineWidth(mCaptionOutlineWidthValue);
.setUsedOutlineFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setHasOutline(true);
.setOutlineColor(mCaptionOutlineColorList.get(pos).mColorValue);
mCaptionDataListClone.get(index).setOutlineWidth(mCaptionOutlineWidthValue);
mCaptionDataListClone.get(index).setOutlineColorAlpha(mCaptionOutlineOpacityValue);
mCurAddCaption.setOutlineWidth(width);
if (index >= 0) {
mCaptionDataListClone.get(index).setOutlineWidth(mCaptionOutlineWidthValue);
NvsColor curColor = mCurAddCaption.getOutlineColor();
mCurAddCaption.setOutlineColor(curColor);
if (index >= 0) {
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-193` `initCaptionBackgroundFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2362`

API classes: `NvsColor`
Common calls: `get()`, `abs()`, `setUsedBackgroundFlag()`, `setCaptionBackground()`, `setBackgroundColor()`, `updateCaptionOpacityValue()`, `getBackgroundColor()`, `nvsColorToHexString()`, `notifyDataSetChanged()`, `getTextBoundingRect()`, `initCaptionMaxCorner()`, `getBackgroundRadius()`

Simple sequence:

```java
mCaptionBackgroundFragment.applyToAllCaption(bIsCaptionBackgroundApplyToAll);
mCaptionDataListClone.get(index).getCaptionBackgroundAlpha();
NvsColor curColor = mCurAddCaption.getBackgroundColor();
mCaptionBackgroundFragment.setCaptionBackgroundInfolist(mCaptionBackgroundList);
RectF rectF = mCurAddCaption.getTextBoundingRect();
if (mCurAddCaption != null) {
mCaptionBackgroundCornerValue = mCurAddCaption.getBackgroundRadius();
if (mCurAddCaption != null) {
mCaptionBackgroundPeddingValue = mCurAddCaption.getBoundaryPaddingRatio();
NvsColor color = ColorUtil.colorStringtoNvsColor(noColor);
mCurAddCaption.setBackgroundColor(color);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setCaptionBackground(noColor);
NvsColor color =
mCurAddCaption.setBackgroundColor(color);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
.setCaptionBackground(mCaptionBackgroundList.get(pos).mColorValue);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
.setCaptionBackground(mCaptionBackgroundList.get(pos).mColorValue);
mCaptionBackgroundCornerValue = mCurAddCaption.getBackgroundRadius();
NvsColor curColor = mCurAddCaption.getBackgroundColor();
mCurAddCaption.setBackgroundColor(curColor);
.setUsedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).setCaptionBackground(strColor);
// ... 8 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-194` `initCaptionLetterSpacingFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2740`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setSelectedStandard()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`, `setSelectedMore()`, `setSelectedLarge()`, `setSelectedSmall()`, `OnCaptionLetterSpacingListener()`, `applyToAllCaption()`, `getLetterSpacing()`

Simple sequence:

```java
mCaptionLetterSpacingFragment.applyToAllCaption(bIsLetterSpacingApplyToAll);
float letterSpaceing = mCurAddCaption.getLetterSpacing();
if (letterSpaceing == getLetterSpacing(CAPTION_PERCENT_STANDARD_SPACING)) {
mCaptionLetterSpacingFragment.setSelectedStandard(
mCaptionLetterSpacingFragment.setSelectedMore(
mCaptionLetterSpacingFragment.setSelectedLarge(
mCaptionLetterSpacingFragment.setSelectedSmall(
mCaptionLetterSpacingFragment.setSelectedStandard(
float lineSpacing = mCurAddCaption.getLineSpacing();
if (lineSpacing == CAPTION_SMALL_LINE_SPACING) {
mCaptionLetterSpacingFragment.setSelectedSmall(
mCaptionLetterSpacingFragment.setSelectedStandard(
mCaptionLetterSpacingFragment.setSelectedMore(
mCaptionLetterSpacingFragment.setSelectedLarge(
mCaptionLetterSpacingFragment.setSelectedStandard(
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
// ... 23 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-195` `onSmallBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2790`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
```

## `captions-stickers-196` `onSmallBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2794`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_SMALL_LINE_SPACING);
```

## `captions-stickers-197` `onStandardBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2823`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_STANDARD_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_STANDARD_LINE_SPACING);
```

## `captions-stickers-198` `onStandardBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2827`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_STANDARD_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_STANDARD_LINE_SPACING);
```

## `captions-stickers-199` `onMoreBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2857`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_MORE_LARGE_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_MORE_LARGE_LINE_SPACING);
```

## `captions-stickers-200` `onMoreBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2861`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_MORE_LARGE_LINE_SPACING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_MORE_LARGE_LINE_SPACING);
```

## `captions-stickers-201` `onLargeBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2891`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_LARGE_LINE_SPACEING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_LARGE_LINE_SPACEING);
```

## `captions-stickers-202` `onLargeBtnClicked`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:2895`

API classes: `NvsCaption`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `setLetterSpacing()`, `get()`, `setLineSpacing()`, `setLetterSpacingType()`, `setUsedLetterSpacingFlag()`

Simple sequence:

```java
mCurAddCaption.setLetterSpacingType(NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE);
mCurAddCaption.setLetterSpacing(letterSpace);
if (curCaptionInfo != null) {
curCaptionInfo.setUsedLetterSpacingFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
curCaptionInfo.setLetterSpacing(letterSpace);
mCurAddCaption.setLineSpacing(CAPTION_LARGE_LINE_SPACEING);
if (curCaptionInfo != null) {
curCaptionInfo.setLineSpacing(CAPTION_LARGE_LINE_SPACEING);
```

## `captions-stickers-203` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/caption/ClipCaptionStyleActivity.java:3357`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timestamp,
NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-204` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:337`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setOnClickListener()`, `setOnTitleBarClickListener()`, `setOnProgressChangeListener()`, `OnProgressChangeListener()`, `OnClickListener()`, `setOnFunctionListener()`, `OnFunctionListener()`, `setBooleanVal()`, `setNoiseGrayscale()`, `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mTitleBar.setOnTitleBarClickListener(new OnTitleBarClickListener() {
mCorrectionColorFinish.setOnClickListener(this);
mColorSeekBar.setOnProgressChangeListener(new MagicProgress.OnProgressChangeListener() {
mColorResetImageView.setOnClickListener(new View.OnClickListener() {
mDenoiseAdjustView.setOnFunctionListener(new DenoiseAdjustView.OnFunctionListener() {
mCurrentVideoFx.setBooleanVal(Constants.ADJUST_DENOISE_COLOR_MODE, denoiseSingleColor);
correctionColorInfo.setNoiseGrayscale(denoiseSingleColor);
if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (null != mCurrentAdjustItem) {
mCurrentAdjustItem.setDefaultValue(0);
mCurrentAdjustItem.setExtra(0);
resetAdjustData(Constants.ADJUST_DENOISE, mCurrentAdjustItem.getDefaultValue());
resetAdjustData(Constants.ADJUST_DENOISE_DENSITY, mCurrentAdjustItem.getExtra());
```

## `captions-stickers-205` `onSelectMode`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:380`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-206` `onAdjustDataChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:416`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFloatVal()`, `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mCurrentVideoFx.setFloatVal(mCurrentColorType, colorVal);
if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-207` `onAdjustDataChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:417`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFloatVal()`, `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mCurrentVideoFx.setFloatVal(mCurrentColorType, colorVal);
if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-208` `onAdjustDataChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:421`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-209` `resetAdjustData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:485`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `equals()`, `setFloatVal()`, `setDenoiseProgress()`, `setDenoiseDensityProgress()`, `setBooleanVal()`, `setNoiseGrayscale()`, `setProgress()`, `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mCurrentVideoFx.setFloatVal(mCurrentColorType, defaultValue);
if (mCurrentColorType.equals(Constants.ADJUST_DENOISE)) {
mDenoiseAdjustView.setDenoiseProgress(progress);
mDenoiseAdjustView.setDenoiseDensityProgress(progress);
mCurrentVideoFx.setBooleanVal(mCurrentColorType, defaultValue == 0);
mDenoiseAdjustView.setNoiseGrayscale(defaultValue == 0);
mColorSeekBar.setProgress(progress);
if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-210` `resetAdjustData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:486`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `equals()`, `setFloatVal()`, `setDenoiseProgress()`, `setDenoiseDensityProgress()`, `setBooleanVal()`, `setNoiseGrayscale()`, `setProgress()`, `getCurrentEngineState()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mCurrentVideoFx.setFloatVal(mCurrentColorType, defaultValue);
if (mCurrentColorType.equals(Constants.ADJUST_DENOISE)) {
mDenoiseAdjustView.setDenoiseProgress(progress);
mDenoiseAdjustView.setDenoiseDensityProgress(progress);
mCurrentVideoFx.setBooleanVal(mCurrentColorType, defaultValue == 0);
mDenoiseAdjustView.setNoiseGrayscale(defaultValue == 0);
mColorSeekBar.setProgress(progress);
if (mClipFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-211` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:588`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `putInt()`, `getLayoutParams()`, `beginTransaction()`, `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `seekTimeline()`, `getTimelineCurrentPosition()`, `setTimeline()`, `instance()`, `getMakeRatio()`, `setArguments()`, `add()`

Simple sequence:

```java
mClipFragment.setFragmentLoadFinisedListener(new SingleClipFragment.OnFragmentLoadFinisedListener() {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
mClipFragment.setTimeline(mTimeline);
bundle.putInt("titleHeight", mTitleBar.getLayoutParams().height);
bundle.putInt("bottomHeight", mBottomLayout.getLayoutParams().height);
bundle.putInt("ratio", TimelineData.instance().getMakeRatio());
mClipFragment.setArguments(bundle);
```

## `captions-stickers-212` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/correctionColor/CorrectionColorActivity.java:592`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-213` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:219`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsVideoClip`, `NvsTimelineTimeSpan`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getDuration()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getScreenWidth()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();
for (int index = 0; index < clipCount; ++index) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
sequenceDescs.mediaFilePath = videoClip.getFilePath();
sequenceDescs.trimIn = videoClip.getTrimIn();
sequenceDescs.trimOut = videoClip.getTrimOut();
sequenceDescs.inPoint = videoClip.getInPoint();
sequenceDescs.outPoint = videoClip.getOutPoint();
long duration = mTimeline.getDuration();
int halfScreenWidth = ScreenUtils.getScreenWidth(this) / 2;
RelativeLayout.LayoutParams layoutParams = (RelativeLayout.LayoutParams) mPlayBtnLayout.getLayoutParams();
mTimelineEditor.setSequencLeftPadding(sequenceLeftPadding);
mTimelineEditor.setSequencRightPadding(halfScreenWidth);
mTimelineEditor.setTimeSpanLeftPadding(sequenceLeftPadding);
mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");
timelineTimeSpan = mTimelineEditor.addTimeSpan(0, mTimeline.getDuration());
timelineTimeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
```

## `captions-stickers-214` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:282`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.setFragmentLoadFinisedListener(new SingleClipFragment.OnFragmentLoadFinisedListener() {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-215` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/noise/NoiseSuppressionActivity.java:284`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-216` `updateDurationSeekBar`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java:147`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `putInt()`, `getLayoutParams()`, `beginTransaction()`, `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `seekTimeline()`, `getTimelineCurrentPosition()`, `setTimeline()`, `instance()`, `getMakeRatio()`, `setArguments()`, `add()`

Simple sequence:

```java
mClipFragment.setFragmentLoadFinisedListener(new SingleClipFragment.OnFragmentLoadFinisedListener() {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
mClipFragment.setTimeline(mTimeline);
bundle.putInt("titleHeight",mTitleBar.getLayoutParams().height);
bundle.putInt("bottomHeight",mBottomLayout.getLayoutParams().height);
bundle.putInt("ratio", TimelineData.instance().getMakeRatio());
mClipFragment.setArguments(bundle);
```

## `captions-stickers-217` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/DurationActivity.java:151`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-218` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:191`

API classes: `NvsVideoClip`
Static/constants: `NvsVideoClip.IMAGE_CLIP_MOTIONMMODE_ROI`, `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN`
Common calls: `setImageMotionMode()`, `setVisibility()`, `get()`, `setImageMotionROI()`, `setImageMotionAnimationEnabled()`, `seekTimeline()`, `playVideo()`, `getDuration()`, `setNormalStartROI()`, `setNormalEndROI()`, `instance()`, `setClipInfoData()`

Simple sequence:

```java
if (id == R.id.photoSeekButton) {
NvsVideoClip videoClip = getVideoClip();
videoClip.setImageMotionMode(NvsVideoClip.IMAGE_CLIP_MOTIONMMODE_ROI);
videoClip.setImageMotionROI(startRectF, endRectF);
videoClip.setImageMotionMode(NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN);
videoClip.setImageMotionAnimationEnabled(mIsOpenMove);
mClipFragment.seekTimeline(0, 0);
mSeekPhotoVideoLayout.setVisibility(View.VISIBLE);
mClipFragment.playVideo(0, mTimeline.getDuration());
mClipArrayList.get(mCurClipIndex).setNormalStartROI(startRectF);
mClipArrayList.get(mCurClipIndex).setNormalEndROI(endRectF);
BackupData.instance().setClipInfoData(mClipArrayList);
AppManager.getInstance().finishActivity();
mSeekPhotoVideoLayout.setVisibility(View.GONE);
```

## `captions-stickers-219` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:300`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.setFragmentLoadFinisedListener(new SingleClipFragment.OnFragmentLoadFinisedListener() {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-220` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/photo/PhotoMovementActivity.java:302`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-221` `removeTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:531`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `putInt()`, `getLayoutParams()`, `beginTransaction()`, `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `seekTimeline()`, `getTimelineCurrentPosition()`, `setTimeline()`, `instance()`, `getMakeRatio()`, `setArguments()`, `add()`

Simple sequence:

```java
mClipFragment.setFragmentLoadFinisedListener(new SingleClipFragment.OnFragmentLoadFinisedListener() {
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
mClipFragment.setTimeline(mTimeline);
bundle.putInt("titleHeight",mTitleBar.getLayoutParams().height);
bundle.putInt("bottomHeight",mBottomLayout.getLayoutParams().height);
bundle.putInt("ratio", TimelineData.instance().getMakeRatio());
mClipFragment.setArguments(bundle);
```

## `captions-stickers-222` `initClipFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:535`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-223` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:597`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `updateCurPlayTime()`, `seekTimeline()`

Simple sequence:

```java
mClipFragment.seekTimeline(timelinePosition, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-224` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/speed/SpeedActivity.java:598`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `updateCurPlayTime()`, `seekTimeline()`

Simple sequence:

```java
mClipFragment.seekTimeline(timelinePosition, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-225` `SpiltTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/spilt/SpiltTimeSpan.java:42`

API classes: `NvsMultiThumbnailSequenceView`

Simple sequence:

```java
public void setMultiThumbnailSequenceView(NvsMultiThumbnailSequenceView multiThumbnailSequenceView) {
```

## `captions-stickers-226` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:126`

API classes: `NvsTimelineTimeSpanExt`
Static/constants: `NvsTimelineTimeSpanExt.OnTrimInChangeListener`, `NvsTimelineTimeSpanExt.OnTrimOutChangeListener`
Common calls: `setOnChangeListener()`, `getSpeed()`, `get()`, `updateCurPlayTime()`, `updateTotalDuration()`, `OnTrimInChangeListener()`, `changeTrimIn()`, `setVideoTrimIn()`, `OnTrimOutChangeListener()`, `changeTrimOut()`, `setVideoTrimOut()`

Simple sequence:

```java
if(mTimlineTimeSpanExt != null){
mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimInChangeListener() {
if(!fromPicInPic()){
float speed = mClipInfo.getSpeed();
mClipArrayList.get(mCurClipIndex).changeTrimIn(newTrimIn);
mClipFragment.setVideoTrimIn(timeStamp);
mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimOutChangeListener() {
if(!fromPicInPic()){
float speed = mClipInfo.getSpeed();
mClipArrayList.get(mCurClipIndex).changeTrimOut(newTrimOut);
mClipFragment.setVideoTrimOut(timeStamp);
```

## `captions-stickers-227` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/trim/TrimActivity.java:127`

API classes: `NvsTimelineTimeSpanExt`
Static/constants: `NvsTimelineTimeSpanExt.OnTrimInChangeListener`
Common calls: `setOnChangeListener()`, `OnTrimInChangeListener()`, `getSpeed()`, `get()`, `changeTrimIn()`, `updateCurPlayTime()`, `setVideoTrimIn()`, `updateTotalDuration()`

Simple sequence:

```java
mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimInChangeListener() {
if(!fromPicInPic()){
float speed = mClipInfo.getSpeed();
mClipArrayList.get(mCurClipIndex).changeTrimIn(newTrimIn);
mClipFragment.setVideoTrimIn(timeStamp);
```

## `captions-stickers-228` `onStopTrackingTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:310`

API classes: `NvsTimelineEditor`, `NvsStreamingContext`
Static/constants: `NvsTimelineEditor.OnScrollChangeListener`, `NvsStreamingContext.getInstance`
Common calls: `getTimelineCurrentPosition()`, `setOnScrollListener()`, `OnScrollChangeListener()`, `getAction()`, `setTimelineScaleForSeek()`, `getDurationWidth()`, `unSelectAllTimeSpan()`, `seekTimeline()`, `getInstance()`, `getVisibility()`

Simple sequence:

```java
mTimelineEditor.setOnScrollListener(new NvsTimelineEditor.OnScrollChangeListener() {
switch (event.getAction()) {
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
if (mTimeline != null) {
mClipFragment.seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline), 0);
if (llKeyFrame.getVisibility() == View.VISIBLE) {
updateVolumeRelativeView(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-229` `onScrollX`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:317`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getTimelineCurrentPosition()`, `getAction()`, `setTimelineScaleForSeek()`, `getDurationWidth()`, `unSelectAllTimeSpan()`, `seekTimeline()`, `getInstance()`, `getVisibility()`

Simple sequence:

```java
switch (event.getAction()) {
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
if (mTimeline != null) {
mClipFragment.seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline), 0);
if (llKeyFrame.getVisibility() == View.VISIBLE) {
updateVolumeRelativeView(mStreamingContext.getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-230` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:401`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsVideoClip`, `NvsTimelineTimeSpan`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getDuration()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getScreenWidth()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();
for (int index = 0; index < clipCount; ++index) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
sequenceDescs.mediaFilePath = videoClip.getFilePath();
sequenceDescs.trimIn = videoClip.getTrimIn();
sequenceDescs.trimOut = videoClip.getTrimOut();
sequenceDescs.inPoint = videoClip.getInPoint();
sequenceDescs.outPoint = videoClip.getOutPoint();
long duration = mTimeline.getDuration();
int halfScreenWidth = ScreenUtils.getScreenWidth(this) / 2;
RelativeLayout.LayoutParams layoutParams = (RelativeLayout.LayoutParams) mPlayBtnLayout.getLayoutParams();
mTimelineEditor.setSequencLeftPadding(sequenceLeftPadding);
mTimelineEditor.setSequencRightPadding(halfScreenWidth);
mTimelineEditor.setTimeSpanLeftPadding(sequenceLeftPadding);
mTimelineEditor.setTimeSpanType("NvsTimelineTimeSpan");
timelineTimeSpan = mTimelineEditor.addTimeSpan(0, mTimeline.getDuration());
timelineTimeSpan.getTimeSpanshadowView().setBackgroundColor(getResources().getColor(R.color.red_4fea));
```

## `captions-stickers-231` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/clipEdit/volume/VolumeActivity.java:763`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mClipFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-232` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:222`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-233` `initData`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:239`

API classes: `NvsTimelineEditor`
Common calls: `getMultiThumbnailSequenceView()`, `setPagingEnabled()`

Simple sequence:

```java
mTimelineEditor = (NvsTimelineEditor) findViewById(R.id.caption_timeline_editor);
mMultiSequenceView = mTimelineEditor.getMultiThumbnailSequenceView();
mViewPager.setPagingEnabled(false);
```

## `captions-stickers-234` `initCaptionStyleFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:522`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `stopEngine()`, `putInt()`, `getInstance()`, `setDrawRectVisible()`, `setCaptionStyleListener()`, `OnCaptionStyleListener()`, `setSelectedPos()`, `notifyDataSetChanged()`, `jumpActivityForResult()`, `currentActivity()`, `size()`, `getCurrentEngineState()`

Simple sequence:

```java
captionStyleFragment.setCaptionStyleListener(new CompoundCaptionStyleFragment.OnCaptionStyleListener() {
mCaptionStyleFragment.setSelectedPos(mSelectedStylePos);
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), AssetDownloadActivity.class, bundle, COMPOINDCAPTIONREQUESTLIST);
if (mCurSelectedPos == pos) {
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mAddComCaption != null) {
long startTime = mAddComCaption.getInPoint();
long endTime = mAddComCaption.getOutPoint();
mVideoFragment.setDrawRectVisible(View.GONE);
NvAsset asset = mComCaptionStyleList.get(pos).getAsset();
```

## `captions-stickers-235` `onItemClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:546`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getInPoint()`, `getOutPoint()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mCurSelectedPos == pos) {
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mAddComCaption != null) {
long startTime = mAddComCaption.getInPoint();
long endTime = mAddComCaption.getOutPoint();
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-236` `onItemClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:547`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`
Common calls: `getCurrentEngineState()`, `getInPoint()`, `getOutPoint()`, `playVideo()`, `setDrawRectVisible()`, `stopEngine()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() != NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK) {
if (mAddComCaption != null) {
long startTime = mAddComCaption.getInPoint();
long endTime = mAddComCaption.getOutPoint();
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-237` `initCaptionColorFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:580`

API classes: `NvsColor`
Common calls: `get()`, `getCaptionAttributeList()`, `setTextColor()`, `setM_usedColorFlag()`, `setCaptionColor()`, `notifyDataSetChanged()`, `updateCaptionOpacityValue()`, `getCaptionCount()`, `getInPoint()`, `getOutPoint()`, `setCaptionColorListener()`, `OnCaptionColorListener()`

Simple sequence:

```java
captionColorFragment.setCaptionColorListener(new CompoundCaptionColorFragment.OnCaptionColorListener() {
mCaptionColorFragment.setCaptionColorInfolist(mCaptionColorList);
if (index >= 0) {
NvsColor color = ColorUtil.colorStringtoNvsColor(mCaptionColorList.get(pos).mColorValue);
int count = mCurCaption.getCaptionCount();
for (int i = 0; i < count; i++) {
mCurCaption.setTextColor(i, color);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setM_usedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setCaptionColor(mCaptionColorList.get(pos).mColorValue);
mCurCaption.setTextColor(mSelectedSubCaptionIndex, color);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(mSelectedSubCaptionIndex).setM_usedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(mSelectedSubCaptionIndex).setCaptionColor(mCaptionColorList.get(pos).mColorValue);
playVideo(mCurCaption.getInPoint(), mCurCaption.getOutPoint());
NvsColor curColor = mCurCaption.getTextColor(editIndex);
int count = mCurCaption.getCaptionCount();
for (int i = 0; i < count; i++) {
mCurCaption.setTextColor(i, curColor);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setM_usedColorFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setCaptionColor(strColor);
mCurCaption.setTextColor(mSelectedSubCaptionIndex, curColor);
if (index >= 0) {
// ... 3 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-238` `initCaptionOutlineFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:681`

API classes: `NvsColor`
Common calls: `get()`, `getCaptionAttributeList()`, `getCaptionCount()`, `setDrawOutline()`, `setM_usedOutlineFlag()`, `setOutlineColor()`, `setOutlineWidth()`, `setCaptionStrokeColor()`, `setCaptionStrokeWidth()`, `getInPoint()`, `getOutPoint()`, `notifyDataSetChanged()`

Simple sequence:

```java
captionOutlineFragment.setCaptionOutlineListener(new CompoundCaptionOutlineFragment.OnCaptionOutlineListener() {
mCaptionOutlineFragment.setCaptionOutlineInfolist(mCaptionOutlineColorList);
if (isDrawOutline) {
mCaptionOutlineWidthValue = (int) mCaptionDataListClone.get(index).getOutlineWidth();
mCaptionOutlineOpacityValue = mCaptionDataListClone.get(index).getOutlineColorAlpha();
if (mSelectedSubCaptionIndex < 0) {
int count = mCurCaption.getCaptionCount();
for (int i = 0; i < count; i++) {
mCurCaption.setDrawOutline(false, i);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setM_usedOutlineFlag(CaptionInfo.ATTRIBUTE_UNUSED_FLAG);
mCurCaption.setDrawOutline(false, mSelectedSubCaptionIndex);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(mSelectedSubCaptionIndex).setM_usedOutlineFlag(CaptionInfo.ATTRIBUTE_UNUSED_FLAG);
NvsColor color = ColorUtil.colorStringtoNvsColor(mCaptionOutlineColorList.get(pos).mColorValue);
if (mSelectedSubCaptionIndex < 0) {
int count = mCurCaption.getCaptionCount();
mCurCaption.setDrawOutline(true, i);
mCurCaption.setOutlineColor(color, i);
mCurCaption.setOutlineWidth(mCaptionOutlineWidthValue, i);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setM_usedOutlineFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setCaptionStrokeColor(mCaptionOutlineColorList.get(pos).mColorValue);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setCaptionStrokeWidth(mCaptionOutlineWidthValue);
// ... 31 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-239` `initCaptionBackgroundFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:866`

API classes: `NvsColor`
Common calls: `get()`, `getCaptionAttributeList()`, `setBackgroundColor()`, `setM_usedBackgroundFlag()`, `setCaptionBackgroundColor()`, `nvsColorToHexString()`, `updateCaptionOpacityValue()`, `getBackgroundColor()`, `notifyDataSetChanged()`, `colorStringtoNvsColor()`, `getCaptionCount()`, `getInPoint()`

Simple sequence:

```java
captionBackgroundFragment.setCaptionBackgroundListener(new CompoundCaptionBackgroundFragment.OnCaptionBackgroundListener() {
mCaptionBackgroundOpacityValue = mCaptionDataListClone.get(index).getCaptionBackgroundAlpha();
NvsColor curColor = mCurAddCaption.getBackgroundColor();
mCaptionBackgroundFragment.setCaptionBackgroundInfolist(mCaptionBackgroundList);
NvsColor color = ColorUtil.colorStringtoNvsColor(noColor);
if (mSelectedSubCaptionIndex < 0) {
int count = mCurCaption.getCaptionCount();
for (int i = 0; i < count; i++) {
mCurCaption.setBackgroundColor(color, i);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setM_usedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setCaptionBackgroundColor(noColor);
mCurCaption.setBackgroundColor(color, mSelectedSubCaptionIndex);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(mSelectedSubCaptionIndex).setM_usedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(mSelectedSubCaptionIndex).setCaptionBackgroundColor(noColor);
playVideo(mCurCaption.getInPoint(), mCurCaption.getOutPoint());
NvsColor curColor = mCurCaption.getBackgroundColor(editIndex);
if (mSelectedSubCaptionIndex < 0) {
int count = mCurCaption.getCaptionCount();
for (int i = 0; i < count; i++) {
mCurCaption.setBackgroundColor(curColor, i);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setM_usedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
// ... 8 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-240` `initCaptionBackgroundFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:868`

API classes: `NvsColor`
Common calls: `get()`, `getCaptionBackgroundAlpha()`, `updateCaptionOpacityValue()`, `getBackgroundColor()`, `nvsColorToHexString()`, `setCaptionBackgroundInfolist()`, `notifyDataSetChanged()`

Simple sequence:

```java
mCaptionBackgroundOpacityValue = mCaptionDataListClone.get(index).getCaptionBackgroundAlpha();
NvsColor curColor = mCurAddCaption.getBackgroundColor();
mCaptionBackgroundFragment.setCaptionBackgroundInfolist(mCaptionBackgroundList);
```

## `captions-stickers-241` `onCaptionColor`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:888`

API classes: `NvsColor`
Common calls: `get()`, `getCaptionAttributeList()`, `colorStringtoNvsColor()`, `setBackgroundColor()`, `setM_usedBackgroundFlag()`, `setCaptionBackgroundColor()`, `size()`, `notifyDataSetChanged()`, `nvsColorToHexString()`, `getCaptionCount()`, `updateCaptionOpacityValue()`, `getInPoint()`

Simple sequence:

```java
NvsColor color = ColorUtil.colorStringtoNvsColor(noColor);
if (mSelectedSubCaptionIndex < 0) {
int count = mCurCaption.getCaptionCount();
for (int i = 0; i < count; i++) {
mCurCaption.setBackgroundColor(color, i);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setM_usedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(i).setCaptionBackgroundColor(noColor);
mCurCaption.setBackgroundColor(color, mSelectedSubCaptionIndex);
if (index >= 0) {
mCaptionDataListClone.get(index).getCaptionAttributeList().get(mSelectedSubCaptionIndex).setM_usedBackgroundFlag(CaptionInfo.ATTRIBUTE_USED_FLAG);
mCaptionDataListClone.get(index).getCaptionAttributeList().get(mSelectedSubCaptionIndex).setCaptionBackgroundColor(noColor);
playVideo(mCurCaption.getInPoint(), mCurCaption.getOutPoint());
```

## `captions-stickers-242` `setOnScrollListener`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1119`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING`

Simple sequence:

```java
if (mTimeline != null) {
seekTimeline(timeStamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_ALLOW_FAST_SCRUBBING);
```

## `captions-stickers-243` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1129`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `setTimelineScaleForSeek()`, `getDurationWidth()`, `getInstance()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
if (action == MotionEvent.ACTION_DOWN) {
mTimelineEditor.setTimelineScaleForSeek(mTimeline, mTimelineEditor.getDurationWidth());
seekTimeline(NvsStreamingContext.getInstance().getTimelineCurrentPosition(mTimeline));
```

## `captions-stickers-244` `playBackEOF`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1155`

API classes: `NvsTimeline`

Simple sequence:

```java
public void playStopped(NvsTimeline timeline) {
```

## `captions-stickers-245` `addCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1760`

API classes: `NvsTimelineTimeSpan`
Common calls: `e()`, `add()`, `addCompoundCaption()`, `setZValue()`, `setVisibility()`, `saveCompoundCaptionData()`, `setCaptionStyleUuid()`, `getZValue()`, `playVideo()`, `setDrawRectVisible()`

Simple sequence:

```java
mAddComCaption = mTimeline.addCompoundCaption(mInPoint, mCaptionDuration, captionUuid);
mAddComCaption.setZValue(zVal);
NvsTimelineTimeSpan timeSpan = addTimeSpan(mInPoint, outPoint);
mModifyButton.setVisibility(View.VISIBLE);
if (captionInfo != null) {
captionInfo.setCaptionStyleUuid(captionUuid);
mCurCaptionZVal = (int) mAddComCaption.getZValue();
mVideoFragment.setDrawRectVisible(View.GONE);
```

## `captions-stickers-246` `addAllTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/compoundcaption/CompoundCaptionActivity.java:1870`

API classes: `NvsTimelineTimeSpan`
Common calls: `getInPoint()`, `getOutPoint()`, `add()`, `getNextCaption()`

Simple sequence:

```java
while (caption != null) {
long inPoint = caption.getInPoint();
long outPoint = caption.getOutPoint();
NvsTimelineTimeSpan timeSpan = addTimeSpan(inPoint, outPoint);
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-247` `initMultiSequence`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:247`

API classes: `NvsMultiThumbnailSequenceView`, `NvsVideoTrack`, `NvsVideoClip`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`
Common calls: `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `ThumbnailSequenceDesc()`, `getFilePath()`, `getTrimIn()`, `getTrimOut()`, `getInPoint()`, `getOutPoint()`, `add()`, `getDuration()`, `getLayoutParams()`

Simple sequence:

```java
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
int clipCount = videoTrack.getClipCount();
ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDescsArray = new ArrayList<>();
for (int index = 0; index < clipCount; ++index) {
NvsVideoClip videoClip = videoTrack.getClipByIndex(index);
NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc sequenceDescs = new NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc();
sequenceDescs.mediaFilePath = videoClip.getFilePath();
sequenceDescs.trimIn = videoClip.getTrimIn();
sequenceDescs.trimOut = videoClip.getTrimOut();
sequenceDescs.inPoint = videoClip.getInPoint();
sequenceDescs.outPoint = videoClip.getOutPoint();
long duration = mTimeline.getDuration();
LinearLayout.LayoutParams layoutParams = (LinearLayout.LayoutParams) mVideoPlay.getLayoutParams();
int halfScreenWidth = ScreenUtils.getScreenWidth(this) / 2;
mTimelineEditor.setSequencLeftPadding(sequenceLeftPadding);
mTimelineEditor.setSequencRightPadding(halfScreenWidth);
mTimelineEditor.setTimeSpanLeftPadding(sequenceLeftPadding);
```

## `captions-stickers-248` `seekTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/createPic/CreatePicActivity.java:349`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
mVideoFragment.seekTimeline(timestamp, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-249` `createTimeline`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/filter/FilterPresenter.java:39`

API classes: `NvsTimeline`
Common calls: `createTimeline()`, `applyTheme()`, `instance()`, `getCaptionData()`, `setCaption()`

Simple sequence:

```java
public NvsTimeline createTimeline() {
NvsTimeline timeline = TimelineUtil.createTimeline();
if (timeline == null) {
TimelineUtil.applyTheme(timeline, null);
ArrayList<CaptionInfo> captionArray = TimelineData.instance().getCaptionData();
TimelineUtil.setCaption(timeline, captionArray);
return timeline;
```

## `captions-stickers-250` `applyMaskInfo`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/mask/MaskActivity.java:585`

API classes: `NvsVideoClip`, `NvsVideoTrack`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getBackGroundInfo()`, `getTransX()`, `getTransY()`, `getScaleX()`, `getRotation()`, `buildRealMaskInfoData()`, `getLiveWindow()`, `getFileRatio()`, `getVideoTrackByIndex()`, `getClipCount()`, `getClipByIndex()`, `applyMask()`

Simple sequence:

```java
BackGroundInfo backGroundInfo = clipInfo.getBackGroundInfo();
if (backGroundInfo != null) {
transX = backGroundInfo.getTransX();
transY = backGroundInfo.getTransY();
scaleX = backGroundInfo.getScaleX();
rotation = backGroundInfo.getRotation();
NvMaskHelper.buildRealMaskInfoData(maskInfoData, mVideoFragment.getLiveWindow(), rotation,
transX, transY, scaleX, clipInfo.getFileRatio());
NvsVideoTrack videoTrack = mTimeline.getVideoTrackByIndex(0);
NvsVideoClip videoClip = null;
int clipCount = videoTrack.getClipCount();
for (int i = 0; i < clipCount; i++) {
NvsVideoClip clipByIndex = videoTrack.getClipByIndex(i);
TimelineUtil.applyMask(videoClip, maskInfoData);
mVideoFragment.seekTimeline(videoClip.getInPoint(), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-251` `setVolumeGain`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/record/RecordActivity.java:573`

API classes: `NvsVideoTrack`, `NvsAudioTrack`, `NvsTimelineAnimatedSticker`
Common calls: `setVolumeGain()`, `getVideoTrackByIndex()`, `getAudioTrackByIndex()`, `setThemeMusicVolumeGain()`, `getFirstAnimatedSticker()`, `hasAudio()`, `getNextAnimatedSticker()`

Simple sequence:

```java
NvsVideoTrack videoTrack = m_timeLine.getVideoTrackByIndex(0);
if (videoTrack != null) {
videoTrack.setVolumeGain(videoLeftVolume, videoLeftVolume);
NvsAudioTrack musicTrack = m_timeLine.getAudioTrackByIndex(0);
if (musicTrack != null) {
musicTrack.setVolumeGain(musicLeftVolume, musicLeftVolume);
m_timeLine.setThemeMusicVolumeGain(themeLeftVolume, themeLeftVolume);
NvsTimelineAnimatedSticker sticker = m_timeLine.getFirstAnimatedSticker();
if (sticker.hasAudio()) {
sticker.setVolumeGain(stickerLeftVolume, stickerLeftVolume);
sticker = m_timeLine.getNextAnimatedSticker(sticker);
```

## `captions-stickers-252` `streamingEngineStateChanged`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:150`

API classes: `NvsStreamingContext`, `NvsTimelineCaption`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsTimelineCaption.ROLE_IN_THEME_TITLE`, `NvsTimelineCaption.ROLE_IN_THEME_TRAILER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `instance()`, `getRoleInTheme()`, `setAssetEditListener()`, `AssetEditListener()`, `getCurrentEngineState()`, `curPointIsInnerDrawRect()`, `OnCloseListener()`, `getUserInputText()`, `setThemeCptionTitle()`, `setThemeCptionTrailer()`, `applyTheme()`, `getCaptionData()`

Simple sequence:

```java
mVideoFragment.setAssetEditListener(new VideoFragment.AssetEditListener() {
if (mVideoFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)
String userInputText = d.getUserInputText();
if (mThemeCaption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {
TimelineData.instance().setThemeCptionTitle(userInputText);
} else if (mThemeCaption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TRAILER) {
TimelineData.instance().setThemeCptionTrailer(userInputText);
TimelineUtil.applyTheme(mTimeline, mThemeId);
ArrayList<CaptionInfo> captionArray = TimelineData.instance().getCaptionData();
TimelineUtil.setCaption(mTimeline, captionArray);
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-253` `onAssetDelete`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:156`

API classes: `NvsStreamingContext`, `NvsTimelineCaption`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK`, `NvsTimelineCaption.ROLE_IN_THEME_TITLE`, `NvsTimelineCaption.ROLE_IN_THEME_TRAILER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `instance()`, `getRoleInTheme()`, `getCurrentEngineState()`, `curPointIsInnerDrawRect()`, `OnCloseListener()`, `getUserInputText()`, `setThemeCptionTitle()`, `setThemeCptionTrailer()`, `applyTheme()`, `getCaptionData()`, `setCaption()`, `seekTimeline()`

Simple sequence:

```java
if (mVideoFragment.getCurrentEngineState() == NvsStreamingContext.STREAMING_ENGINE_STATE_PLAYBACK)
String userInputText = d.getUserInputText();
if (mThemeCaption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {
TimelineData.instance().setThemeCptionTitle(userInputText);
} else if (mThemeCaption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TRAILER) {
TimelineData.instance().setThemeCptionTrailer(userInputText);
TimelineUtil.applyTheme(mTimeline, mThemeId);
ArrayList<CaptionInfo> captionArray = TimelineData.instance().getCaptionData();
TimelineUtil.setCaption(mTimeline, captionArray);
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-254` `onClick`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:221`

API classes: `NvsVideoClip`
Static/constants: `NvsVideoClip.ROLE_IN_THEME_TITLE`, `NvsVideoClip.ROLE_IN_THEME_TRAILER`
Common calls: `instance()`, `putInt()`, `getInstance()`, `getClipByIndex()`, `getRoleInTheme()`, `remove()`, `add()`, `setClickable()`, `jumpActivityForResult()`, `currentActivity()`, `getClipCount()`, `getTransitionInfoArray()`

Simple sequence:

```java
if (id == R.id.download_more_btn) {
mDownloadMoreBtn.setClickable(false);
AppManager.getInstance().jumpActivityForResult(AppManager.getInstance().currentActivity(), AssetDownloadActivity.class, bundle, THEMEREQUESTLIST);
int afterThemeClipsCount = mVidoeTrack.getClipCount();
NvsVideoClip afterThemeFirstClip = mVidoeTrack.getClipByIndex(0);
boolean hasThemeTitle = (afterThemeFirstClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TITLE);
NvsVideoClip afterThemeLastClip = mVidoeTrack.getClipByIndex(afterThemeClipsCount - 1);
boolean hasThemeTrailer = (afterThemeLastClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TRAILER);
ArrayList<TransitionInfo> transitionInfoArray = TimelineData.instance().getTransitionInfoArray();
TimelineData.instance().setThemeData(mThemeId);
TimelineData.instance().setCaptionData(mCaptionDataListClone);
TimelineData.instance().setTransitionInfoArray(null);
```

## `captions-stickers-255` `onDestroy`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:311`

API classes: `NvsVideoClip`
Static/constants: `NvsVideoClip.ROLE_IN_THEME_TITLE`, `NvsVideoClip.ROLE_IN_THEME_TRAILER`
Common calls: `getClipByIndex()`, `getRoleInTheme()`, `instance()`, `createTimeline()`, `getVideoTrackByIndex()`, `getClipCount()`, `cloneCaptionData()`, `getThemeData()`, `getDuration()`, `sharedInstance()`, `searchLocalAssets()`, `searchReservedAssets()`

Simple sequence:

```java
mTimeline = TimelineUtil.createTimeline();
if (mTimeline == null)
mVidoeTrack = mTimeline.getVideoTrackByIndex(0);
mCurentClipCount = mVidoeTrack.getClipCount();
NvsVideoClip theFirstClip = mVidoeTrack.getClipByIndex(0);
NvsVideoClip theLastClip = mVidoeTrack.getClipByIndex(mCurentClipCount - 1);
mHasThemeTitle = (theFirstClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TITLE);
mHasThemeTrailer = (theLastClip.getRoleInTheme() == NvsVideoClip.ROLE_IN_THEME_TRAILER);
mThemeId = TimelineData.instance().getThemeData();
mTotalDuration = mTimeline.getDuration();
```

## `captions-stickers-256` `isHasThemeCaptionTitle`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:573`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_TITLE`
Common calls: `getFirstCaption()`, `getCategory()`, `getRoleInTheme()`, `getNextCaption()`

Simple sequence:

```java
NvsTimelineCaption caption = mTimeline.getFirstCaption();
if (caption.getCategory() == NvsTimelineCaption.THEME_CATEGORY
&& caption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-257` `isHasThemeCaptionTitle`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:575`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_TITLE`
Common calls: `getCategory()`, `getRoleInTheme()`, `getNextCaption()`

Simple sequence:

```java
if (caption.getCategory() == NvsTimelineCaption.THEME_CATEGORY
&& caption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-258` `isHasThemeCaptionTitle`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:578`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.ROLE_IN_THEME_TITLE`
Common calls: `getRoleInTheme()`

Simple sequence:

```java
&& caption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {
```

## `captions-stickers-259` `selectThemeCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:590`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `get()`, `getTimelineCurrentPosition()`, `getCaptionsByTimelinePosition()`, `size()`, `getCategory()`, `getRoleInTheme()`

Simple sequence:

```java
long curPos = mStreamingContext.getTimelineCurrentPosition(mTimeline);
List<NvsTimelineCaption> captionList = mTimeline.getCaptionsByTimelinePosition(curPos);
for (int i = 0; i < captionCount; i++) {
NvsTimelineCaption caption = captionList.get(i);
if (caption.getCategory() == NvsTimelineCaption.THEME_CATEGORY
&& caption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
```

## `captions-stickers-260` `selectThemeCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/theme/ThemeActivity.java:594`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `get()`, `getCategory()`, `getRoleInTheme()`

Simple sequence:

```java
for (int i = 0; i < captionCount; i++) {
NvsTimelineCaption caption = captionList.get(i);
if (caption.getCategory() == NvsTimelineCaption.THEME_CATEGORY
&& caption.getRoleInTheme() != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
```

## `captions-stickers-261` `initTimelineEditor`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:143`

API classes: `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt`, `NvsTimelineTimeSpan`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`, `NvsMultiThumbnailSequenceView.OnScrollChangeListener`
Common calls: `size()`, `scrollTo()`, `addView()`, `mapTimelinePosFromX()`, `getParent()`, `setThumbnailSequenceDescArray()`, `setPixelPerMicrosecond()`, `setStartPadding()`, `setEndPadding()`, `LayoutParams()`, `setOnTouchListener()`, `onTouch()`

Simple sequence:

```java
public void initTimelineEditor(ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDesc, final long timelineDuration) {
m_multiThumbnailSequenceView.setThumbnailSequenceDescArray(sequenceDesc);
m_multiThumbnailSequenceView.setPixelPerMicrosecond(m_pixelPerMicrosecond);
m_multiThumbnailSequenceView.setStartPadding(m_sequencLeftPadding);
m_multiThumbnailSequenceView.setEndPadding(m_sequencRightPadding);
m_multiThumbnailSequenceView.setOnTouchListener(new OnTouchListener() {
m_multiThumbnailSequenceView.setOnScrollChangeListenser(new NvsMultiThumbnailSequenceView.OnScrollChangeListener() {
public void onScrollChanged(NvsMultiThumbnailSequenceView nvsMultiThumbnailSequenceView, int i, int i1) {
if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") == 0) {
NvsTimelineTimeSpan timeSpan = m_timelineTimeSpanArray.get(index);
long inPoint = timeSpan.getInPoint();
long outPoint = timeSpan.getOutPoint();
if (add) {
if (timeSpan.getParent() == null) {
if (timeSpan.getParent() != null) {
m_timeSpanRelativeLayout.removeView(timeSpan);
```

## `captions-stickers-262` `addTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:214`

API classes: `NvsTimelineTimeSpan`
Common calls: `floor()`, `setMinTimeSpanPixel()`, `setMaxTimeSpanPixel()`

Simple sequence:

```java
public NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
NvsTimelineTimeSpan timelineTimeSpan = createTimeSpan(inPoint, outPoint);
timelineTimeSpan.setMinTimeSpanPixel(minTimeSpanPixel);
timelineTimeSpan.setMaxTimeSpanPixel(maxTimeSpanPixel);
```

## `captions-stickers-263` `addDouVideoTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:231`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnMarginChangeListener`
Common calls: `floor()`, `setMargins()`, `setBackgroundColor()`, `setBackgroundResource()`, `LayoutParams()`, `addRule()`, `addView()`, `getLayoutParams()`, `setLayoutParams()`, `getLeftHandleView()`, `getRightHandleView()`, `getTimeSpanshadowView()`

Simple sequence:

```java
public NvsTimelineTimeSpan addDouVideoTimeSpan(long inPoint, long outPoint) {
NvsTimelineTimeSpan timelineTimeSpan = createTimeSpan(inPoint, outPoint);
if (timelineTimeSpan != null) {
timelineTimeSpan.getLeftHandleView().setBackgroundResource(R.mipmap.trimline_select_left);
timelineTimeSpan.getRightHandleView().setBackgroundResource(R.mipmap.trimline_select_right);
timelineTimeSpan.getTimeSpanshadowView().setBackgroundColor(Color.TRANSPARENT);
timelineTimeSpan.setMinTimeSpanPixel(minTimeSpanPixel);
timelineTimeSpan.setMaxTimeSpanPixel(maxTimeSpanPixel);
viewLeftMargin.setBackgroundColor(backgrdColor);
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - shadowMarginWidth, 0);
viewRightMargin.setBackgroundColor(backgrdColor);
viewRightMarginParams.setMargins(shadowMarginWidth + spanWidth, 0, 0, 0);
timelineTimeSpan.setMarginChangeListener(new NvsTimelineTimeSpan.OnMarginChangeListener() {
RelativeLayout.LayoutParams viewLeftMarginParams = (RelativeLayout.LayoutParams) viewLeftMargin.getLayoutParams();
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - leftMargin, 0);
viewLeftMargin.setLayoutParams(viewLeftMarginParams);
RelativeLayout.LayoutParams viewRightMarginParams = (RelativeLayout.LayoutParams) viewRightMargin.getLayoutParams();
viewRightMarginParams.setMargins(leftMargin + timeSpanWidth, 0, 0, 0);
viewRightMargin.setLayoutParams(viewRightMarginParams);
```

## `captions-stickers-264` `addDouVideoTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:233`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnMarginChangeListener`
Common calls: `floor()`, `setMargins()`, `setBackgroundColor()`, `setBackgroundResource()`, `LayoutParams()`, `addRule()`, `addView()`, `getLayoutParams()`, `setLayoutParams()`, `getLeftHandleView()`, `getRightHandleView()`, `getTimeSpanshadowView()`

Simple sequence:

```java
if (timelineTimeSpan != null) {
timelineTimeSpan.getLeftHandleView().setBackgroundResource(R.mipmap.trimline_select_left);
timelineTimeSpan.getRightHandleView().setBackgroundResource(R.mipmap.trimline_select_right);
timelineTimeSpan.getTimeSpanshadowView().setBackgroundColor(Color.TRANSPARENT);
timelineTimeSpan.setMinTimeSpanPixel(minTimeSpanPixel);
timelineTimeSpan.setMaxTimeSpanPixel(maxTimeSpanPixel);
viewLeftMargin.setBackgroundColor(backgrdColor);
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - shadowMarginWidth, 0);
viewRightMargin.setBackgroundColor(backgrdColor);
viewRightMarginParams.setMargins(shadowMarginWidth + spanWidth, 0, 0, 0);
timelineTimeSpan.setMarginChangeListener(new NvsTimelineTimeSpan.OnMarginChangeListener() {
RelativeLayout.LayoutParams viewLeftMarginParams = (RelativeLayout.LayoutParams) viewLeftMargin.getLayoutParams();
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - leftMargin, 0);
viewLeftMargin.setLayoutParams(viewLeftMarginParams);
RelativeLayout.LayoutParams viewRightMarginParams = (RelativeLayout.LayoutParams) viewRightMargin.getLayoutParams();
viewRightMarginParams.setMargins(leftMargin + timeSpanWidth, 0, 0, 0);
viewRightMargin.setLayoutParams(viewRightMarginParams);
```

## `captions-stickers-265` `addTimeSpanExt`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:292`

API classes: `NvsTimelineTimeSpanExt`
Static/constants: `NvsTimelineTimeSpanExt.OnMarginChangeListener`
Common calls: `setMargins()`, `LayoutParams()`, `setLayoutParams()`, `addView()`, `floor()`, `setBackgroundColor()`, `addRule()`, `getLayoutParams()`, `compareTo()`, `setMultiThumbnailSequenceView()`, `setInPoint()`, `setOutPoint()`

Simple sequence:

```java
public NvsTimelineTimeSpanExt addTimeSpanExt(long inPoint, long outPoint) {
if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") != 0)
NvsTimelineTimeSpanExt timeSpanExt = new NvsTimelineTimeSpanExt(m_context);
timeSpanExt.setMultiThumbnailSequenceView(m_multiThumbnailSequenceView);
timeSpanExt.setInPoint(inPoint);
timeSpanExt.setOutPoint(outPoint);
timeSpanExt.setPixelPerMicrosecond(m_pixelPerMicrosecond);
int lLeftHandleWidth = timeSpanExt.getLLeftHandleWidth();
timeSpanExt.setTotalWidth(totalWidth);
spanItemParams.setMargins(leftMargin, RelativeLayout.LayoutParams.MATCH_PARENT, totalWidth - (leftMargin + spanWidth), 0);
timeSpanExt.setLayoutParams(spanItemParams);
viewLeftMargin.setBackgroundColor(backgrdColor);
int tmpMarginHeight = timeSpanExt.getLTopHandleHeight();
viewLeftMarginParams.setMargins(tmpLLeftHandleWidth, 0, tmpTotalWidth - tmpLLeftHandleWidth - leftMargin, 0);
viewRightMargin.setBackgroundColor(backgrdColor);
viewRightMarginParams.setMargins(leftMargin + spanWidth - lLeftHandleWidth, 0, lLeftHandleWidth, 0);
timeSpanExt.setMarginChangeListener(new NvsTimelineTimeSpanExt.OnMarginChangeListener() {
RelativeLayout.LayoutParams viewLeftMarginParams = (RelativeLayout.LayoutParams) viewLeftMargin.getLayoutParams();
viewLeftMarginParams.setMargins(tmpLLeftHandleWidth, 0, tmpTotalWidth - leftMargin, 0);
viewLeftMargin.setLayoutParams(viewLeftMarginParams);
RelativeLayout.LayoutParams viewRightMarginParams = (RelativeLayout.LayoutParams) viewRightMargin.getLayoutParams();
viewRightMarginParams.setMargins(leftMargin + timeSpanWidth, 0, tmpLLeftHandleWidth, 0);
viewRightMargin.setLayoutParams(viewRightMarginParams);
```

## `captions-stickers-266` `selectTimeSpan`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:467`

API classes: `NvsTimelineTimeSpan`
Common calls: `setHasSelected()`, `requestLayout()`, `bringToFront()`

Simple sequence:

```java
public void selectTimeSpan(NvsTimelineTimeSpan timeSpan) {
timeSpan.setHasSelected(true);
```

## `captions-stickers-267` `timeSpanCount`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/timelineEditor/NvsTimelineEditor.java:486`

API classes: `NvsTimelineTimeSpan`
Common calls: `getChildCount()`, `removeView()`, `remove()`

Simple sequence:

```java
public void deleteSelectedTimeSpan(NvsTimelineTimeSpan timeSpan) {
int count = m_timeSpanRelativeLayout.getChildCount();
if (count > 0) {
m_timeSpanRelativeLayout.removeView(timeSpan);
```

## `captions-stickers-268` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:470`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFragmentLoadFinisedListener()`, `OnFragmentLoadFinisedListener()`, `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mVideoFragment.setFragmentLoadFinisedListener(new VideoFragment.OnFragmentLoadFinisedListener() {
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline),
NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-269` `initVideoFragment`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/transition/TransitionActivity.java:472`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `seekTimeline()`, `getTimelineCurrentPosition()`

Simple sequence:

```java
mVideoFragment.seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline),
NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-270` `onBackPressed`

Source: `app/src/main/java/com/meishe/sdkdemo/edit/watermark/SingleClickActivity.java:448`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER`
Common calls: `sharedInstance()`, `toString()`, `installAssetPackage()`, `isEmpty()`, `NvCustomStickerInfo()`, `randomUUID()`, `getUsableCustomStickerAssets()`, `size()`, `appendCustomStickerInfoData()`, `setCustomStickerInfoToSharedPreferences()`, `start()`

Simple sequence:

```java
String packageId = PackageManagerUtil.installAssetPackage(stickerTemplatePath, null, NvsAssetPackageManager.ASSET_PACKAGE_TYPE_ANIMATEDSTICKER);
customStickerInfo.order = NvAssetManager.sharedInstance().getUsableCustomStickerAssets().size();
NvAssetManager.sharedInstance().setCustomStickerInfoToSharedPreferences();
```

## `captions-stickers-271` `bindLayout`

Source: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:200`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.getInstance`
Common calls: `getInstance()`, `addActivity()`, `getWriteReadPermission()`

Simple sequence:

```java
AppManager.getInstance().addActivity(this);
mStreamingContext = NvsStreamingContext.getInstance();
permissionList = Util.getWriteReadPermission();
```

## `captions-stickers-272` `onTouch`

Source: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:296`

API classes: `NvsTimeline`
Common calls: `setVisibility()`, `setCompileVideoListener()`, `OnCompileVideoListener()`

Simple sequence:

```java
if (mCompileVideoFragment != null) {
mCompileVideoFragment.setCompileVideoListener(new CompileVideoFragment.OnCompileVideoListener() {
public void compileProgress(NvsTimeline timeline, int progress) {
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `captions-stickers-273` `compileProgress`

Source: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:304`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFinished(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `captions-stickers-274` `compileFinished`

Source: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:309`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileFailed(NvsTimeline timeline) {
mCompilePage.setVisibility(View.GONE);
```

## `captions-stickers-275` `compileFailed`

Source: `app/src/main/java/com/meishe/sdkdemo/flipcaption/FlipCaptionActivity.java:314`

API classes: `NvsTimeline`
Common calls: `setVisibility()`

Simple sequence:

```java
public void compileCompleted(NvsTimeline nvsTimeline, boolean isCanceled) {
mCompilePage.setVisibility(View.GONE);
```

## `captions-stickers-276` `addCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/musicLyrics/MusicLyricsActivity.java:260`

API classes: `NvsTimelineCaption`
Common calls: `getLastCaption()`, `getNextCaption()`, `removeCaption()`

Simple sequence:

```java
while (first != mTimeline.getLastCaption()) {
NvsTimelineCaption next = mTimeline.getNextCaption(first);
mTimeline.removeCaption(first);
```

## `captions-stickers-277` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:147`

API classes: `NvsTimelineTimeSpanExt`
Static/constants: `NvsTimelineTimeSpanExt.OnTrimInChangeListener`, `NvsTimelineTimeSpanExt.OnTrimOutChangeListener`
Common calls: `setOnChangeListener()`, `OnTrimInChangeListener()`, `changeTrimIn()`, `updateCurPlayTime()`, `setVideoTrimIn()`, `OnTrimOutChangeListener()`, `changeTrimOut()`, `setVideoTrimOut()`

Simple sequence:

```java
if (mTimlineTimeSpanExt != null) {
mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimInChangeListener() {
mClipInfo.changeTrimIn(mTrimInPoint);
mClipFragment.setVideoTrimIn(timeStamp);
mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimOutChangeListener() {
mClipInfo.changeTrimOut(mTrimOutPoint);
mClipFragment.setVideoTrimOut(timeStamp);
```

## `captions-stickers-278` `initListener`

Source: `app/src/main/java/com/meishe/sdkdemo/quicksplicing/FileQuickSplicingActivity.java:148`

API classes: `NvsTimelineTimeSpanExt`
Static/constants: `NvsTimelineTimeSpanExt.OnTrimInChangeListener`
Common calls: `setOnChangeListener()`, `OnTrimInChangeListener()`, `changeTrimIn()`, `updateCurPlayTime()`, `setVideoTrimIn()`

Simple sequence:

```java
mTimlineTimeSpanExt.setOnChangeListener(new NvsTimelineTimeSpanExt.OnTrimInChangeListener() {
mClipInfo.changeTrimIn(mTrimInPoint);
mClipFragment.setVideoTrimIn(timeStamp);
```

## `captions-stickers-279` `updateCompoundCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:741`

API classes: `NvsCaptureCompoundCaption`
Common calls: `isEmpty()`, `appendCaptureCompoundCaption()`, `e()`, `getDuration()`

Simple sequence:

```java
if (!TextUtils.isEmpty(captionId)) {
NvsCaptureCompoundCaption nvsCaptureCompoundCaption = mStreamingContext.appendCaptureCompoundCaption(0, captionDuration, captionId);
Log.e("meicam", "  === " + nvsCaptureCompoundCaption.getDuration());
```

## `captions-stickers-280` `installAssetPackage`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:814`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`, `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION`
Common calls: `endsWith()`, `installAssetPackage()`

Simple sequence:

```java
int type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
if (filterPackageFilePath.endsWith(".videofx")) {
type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOFX;
if (filterPackageFilePath.endsWith(".compoundcaption")) {
type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
if (filterPackageFilePath.endsWith(".videotransition")) {
type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_VIDEOTRANSITION;
return PackageManagerUtil.installAssetPackage(filterPackageFilePath, null, type);
```

## `captions-stickers-281` `installAssetPackage`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemeCaptureActivity.java:819`

API classes: `NvsAssetPackageManager`
Static/constants: `NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION`
Common calls: `endsWith()`

Simple sequence:

```java
if (filterPackageFilePath.endsWith(".compoundcaption")) {
type = NvsAssetPackageManager.ASSET_PACKAGE_TYPE_COMPOUND_CAPTION;
```

## `captions-stickers-282` `refreshCompoundCaptionView`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:323`

API classes: `NvsTimelineCompoundCaption`
Common calls: `getCaptionCount()`, `setCountIndex()`, `setText()`, `getText()`, `add()`, `setNewDatas()`

Simple sequence:

```java
private void refreshCompoundCaptionView(NvsTimelineCompoundCaption compoundCaption) {
int captionCount = compoundCaption.getCaptionCount();
captionBean.setCountIndex(i);
captionBean.setText(compoundCaption.getText(i));
captionAdapter.setNewDatas(captionBeans);
```

## `captions-stickers-283` `onActivityResult`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:551`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getExtras()`, `setText()`, `getText()`, `onActivityResult()`, `getSerializable()`, `getCaptionBeanByPosition()`, `notifyItemChanged()`, `getCountIndex()`, `seekTimeline()`

Simple sequence:

```java
if (requestCode == CAPTION_RESULT_CODE) {
if (data != null && data.getExtras() != null) {
CaptionBean captionBean = (CaptionBean) data.getExtras().getSerializable("CaptionBean");
if (captionBean != null && currentCompoundCaption != null) {
CaptionBean captionBeanByPosition = captionAdapter.getCaptionBeanByPosition(currentCaption);
captionBeanByPosition.setText(captionBean.getText());
currentCompoundCaption.setText(captionBeanByPosition.getCountIndex(), captionBean.getText());
mStreamingContext.seekTimeline(mTimeline, startDuration, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);
```

## `captions-stickers-284` `onActivityResult`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:553`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getExtras()`, `setText()`, `getText()`, `getSerializable()`, `getCaptionBeanByPosition()`, `notifyItemChanged()`, `getCountIndex()`, `seekTimeline()`

Simple sequence:

```java
if (requestCode == CAPTION_RESULT_CODE) {
if (data != null && data.getExtras() != null) {
CaptionBean captionBean = (CaptionBean) data.getExtras().getSerializable("CaptionBean");
if (captionBean != null && currentCompoundCaption != null) {
CaptionBean captionBeanByPosition = captionAdapter.getCaptionBeanByPosition(currentCaption);
captionBeanByPosition.setText(captionBean.getText());
currentCompoundCaption.setText(captionBeanByPosition.getCountIndex(), captionBean.getText());
mStreamingContext.seekTimeline(mTimeline, startDuration, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);
```

## `captions-stickers-285` `onActivityResult`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:554`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getExtras()`, `setText()`, `getText()`, `getSerializable()`, `getCaptionBeanByPosition()`, `notifyItemChanged()`, `getCountIndex()`, `seekTimeline()`

Simple sequence:

```java
if (requestCode == CAPTION_RESULT_CODE) {
if (data != null && data.getExtras() != null) {
CaptionBean captionBean = (CaptionBean) data.getExtras().getSerializable("CaptionBean");
if (captionBean != null && currentCompoundCaption != null) {
CaptionBean captionBeanByPosition = captionAdapter.getCaptionBeanByPosition(currentCaption);
captionBeanByPosition.setText(captionBean.getText());
currentCompoundCaption.setText(captionBeanByPosition.getCountIndex(), captionBean.getText());
mStreamingContext.seekTimeline(mTimeline, startDuration, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);
```

## `captions-stickers-286` `onActivityResult`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/ThemePreviewActivity.java:555`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `getExtras()`, `setText()`, `getText()`, `getSerializable()`, `getCaptionBeanByPosition()`, `notifyItemChanged()`, `getCountIndex()`, `seekTimeline()`

Simple sequence:

```java
if (data != null && data.getExtras() != null) {
CaptionBean captionBean = (CaptionBean) data.getExtras().getSerializable("CaptionBean");
if (captionBean != null && currentCompoundCaption != null) {
CaptionBean captionBeanByPosition = captionAdapter.getCaptionBeanByPosition(currentCaption);
captionBeanByPosition.setText(captionBean.getText());
currentCompoundCaption.setText(captionBeanByPosition.getCountIndex(), captionBean.getText());
mStreamingContext.seekTimeline(mTimeline, startDuration, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_FULLSIZE, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME);
```

## `captions-stickers-287` `getType`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:85`

API classes: `NvsTimelineCompoundCaption`

Simple sequence:

```java
public NvsTimelineCompoundCaption getCompoundCaption() {
```

## `captions-stickers-288` `getCompoundCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/themeshoot/bean/ThemePreviewBean.java:89`

API classes: `NvsTimelineCompoundCaption`

Simple sequence:

```java
public void setCompoundCaption(NvsTimelineCompoundCaption compoundCaption) {
```

## `captions-stickers-289` `addVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:396`

API classes: `NvsVideoFx`, `NvsVideoClip`, `NvsVideoTrack`, `NvsVideoResolution`
Static/constants: `NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR`, `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE`, `NvsVideoClip.IMAGE_CLIP_MOTIONMMODE_ROI`, `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN`
Common calls: `setFloatVal()`, `appendBuiltinFx()`, `setAttachment()`, `appendClip()`, `e()`, `getTrimIn()`, `getTrimOut()`, `changeTrimOutPoint()`, `setImageMotionMode()`, `changeSpeed()`, `getAbsPathByContentUri()`, `getContext()`

Simple sequence:

```java
private static void addVideoClip(NvsVideoTrack videoTrack, ClipInfo clipInfo, boolean isTrimClip, NvsVideoResolution videoRes) {
String filePath = FileUtils.getAbsPathByContentUri(MSApplication.getContext(),
MSApplication.CONTENT_FLAG, clipInfo.getFilePath());
NvsVideoClip videoClip = null;
LivePhotoInfo livePhotoInfo = clipInfo.getLivePhotoInfo();
if (null != livePhotoInfo) {
String url = livePhotoInfo.getLivePhotoUrl();
videoClip = videoTrack.appendClip(url);
videoClip = videoTrack.appendClip(filePath);
if (blurFlag) {
videoClip.setSourceBackgroundMode(NvsVideoClip.ClIP_BACKGROUNDMODE_BLUR);
CorrectionColorInfo correctionColorInfo = clipInfo.getCorrectionColorInfo();
if (correctionColorInfo != null) {
float brightVal = correctionColorInfo.getBrightnessVal();
float contrastVal = correctionColorInfo.getContrastVal();
float saturationVal = correctionColorInfo.getSaturationVal();
float fade = correctionColorInfo.getFade();
float vignette = correctionColorInfo.getVignetteVal();
float sharpen = correctionColorInfo.getSharpenVal();
float temperature = correctionColorInfo.getTemperature();
float tint = correctionColorInfo.getTint();
float density = correctionColorInfo.getDensity();
float denoiseDensity = correctionColorInfo.getDenoiseDensity();
NvsVideoFx mColorVideoFx = videoClip.appendBuiltinFx(Constants.ADJUST_TYPE_BASIC_IMAGE_ADJUST);
// ... 67 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-290` `addVideoClip`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:568`

API classes: `NvsVideoClip`, `NvsVideoTrack`
Static/constants: `NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE`, `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN`
Common calls: `isEmpty()`, `getAbsPathByContentUri()`, `getContext()`, `appendClip()`, `e()`, `getVideoType()`, `setImageMotionMode()`, `setImageMotionAnimationEnabled()`

Simple sequence:

```java
private static void addVideoClip(NvsVideoTrack videoTrack, String filePath) {
String videoPath = FileUtils.getAbsPathByContentUri(MSApplication.getContext(),
NvsVideoClip videoClip = videoTrack.appendClip(videoPath);
int videoType = videoClip.getVideoType();
if (videoType == NvsVideoClip.VIDEO_CLIP_TYPE_IMAGE) {
videoClip.setImageMotionMode(NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN);
videoClip.setImageMotionAnimationEnabled(false);
```

## `captions-stickers-291` `applyClipAnimatedSticker`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:609`

API classes: `NvsClipAnimatedSticker`, `NvsVideoClip`
Common calls: `getInPoint()`, `getId()`, `getTranslation()`, `setScale()`, `setRotationZ()`, `setTranslation()`, `getFirstAnimatedSticker()`, `removeAnimatedSticker()`, `getOutPoint()`, `isCustomSticker()`, `addCustomAnimatedSticker()`, `getCustomImagePath()`

Simple sequence:

```java
public static void applyClipAnimatedSticker(NvsVideoClip videoClip, List<StickerInfo> stickerInfoList) {
NvsClipAnimatedSticker deleteSticker = videoClip.getFirstAnimatedSticker();
while (deleteSticker != null) {
deleteSticker = videoClip.removeAnimatedSticker(deleteSticker);
for (StickerInfo sticker : stickerInfoList) {
long duration = sticker.getOutPoint() - sticker.getInPoint();
NvsClipAnimatedSticker animatedSticker = isCutsomSticker ?
videoClip.addCustomAnimatedSticker(sticker.getInPoint(), duration, sticker.getId(), sticker.getCustomImagePath())
: videoClip.addAnimatedSticker(sticker.getInPoint(), duration, sticker.getId());
Map<Long, KeyFrameInfo> keyFrameInfoHashMap = sticker.getKeyFrameInfoHashMap();
if (keyFrameInfoHashMap.isEmpty()) {
PointF translation = sticker.getTranslation();
float scaleFactor = sticker.getScaleFactor();
float rotation = sticker.getRotation();
animatedSticker.setScale(scaleFactor);
animatedSticker.setRotationZ(rotation);
animatedSticker.setTranslation(translation);
for (Map.Entry<Long, KeyFrameInfo> entry : entries) {
animatedSticker.setCurrentKeyFrameTime(entry.getKey() - animatedSticker.getInPoint());
KeyFrameInfo keyFrameInfo = entry.getValue();
animatedSticker.setRotationZ(keyFrameInfo.getRotationZ());
animatedSticker.setScale(keyFrameInfo.getScaleX());
animatedSticker.setTranslation(keyFrameInfo.getTranslation());
float volumeGain = sticker.getVolumeGain();
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-292` `applyAnimatedStickerAnimation`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1371`

API classes: `NvsAnimatedSticker`
Common calls: `getPeriodAnimationId()`, `setZValue()`, `getAnimateStickerZVal()`, `setHorizontalFlip()`, `isHorizFlip()`, `isEmpty()`, `applyAnimatedStickerPeriodAnimation()`, `setAnimatedStickerAnimationPeriod()`, `getPeriodAnimationDuration()`, `applyAnimatedStickerInAnimation()`, `getInAnimationId()`, `setAnimatedStickerInAnimationDuration()`

Simple sequence:

```java
public static void applyAnimatedStickerAnimation(NvsAnimatedSticker animatedSticker, StickerInfo stickerInfo) {
animatedSticker.setZValue(stickerInfo.getAnimateStickerZVal());
animatedSticker.setHorizontalFlip(stickerInfo.isHorizFlip());
if (!TextUtils.isEmpty(stickerInfo.getPeriodAnimationId())) {
animatedSticker.applyAnimatedStickerPeriodAnimation(stickerInfo.getPeriodAnimationId());
animatedSticker.setAnimatedStickerAnimationPeriod((int) stickerInfo.getPeriodAnimationDuration());
animatedSticker.applyAnimatedStickerInAnimation(stickerInfo.getInAnimationId());
animatedSticker.setAnimatedStickerInAnimationDuration((int) stickerInfo.getInAnimationDuration());
animatedSticker.applyAnimatedStickerOutAnimation(stickerInfo.getOutAnimationId());
animatedSticker.setAnimatedStickerOutAnimationDuration((int) stickerInfo.getOutAnimationDuration());
```

## `captions-stickers-293` `setCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1396`

API classes: `NvsTimeline`

Simple sequence:

```java
public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray, long themeDuration) {
return setCaption(timeline, captionArray, themeDuration, false);
```

## `captions-stickers-294` `setCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1400`

API classes: `NvsTimelineCaption`, `NvsTimeline`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `getInPoint()`, `getText()`, `getFirstCaption()`, `getCategory()`, `e()`, `getRoleInTheme()`, `getNextCaption()`, `removeCaption()`, `getOutPoint()`, `isTraditionCaption()`, `addCaption()`, `addModularCaption()`

Simple sequence:

```java
public static boolean setCaption(NvsTimeline timeline, ArrayList<CaptionInfo> captionArray, long themeDuration, boolean userRecordingFlag) {
if (timeline == null) {
NvsTimelineCaption deleteCaption = timeline.getFirstCaption();
while (deleteCaption != null) {
int capCategory = deleteCaption.getCategory();
int roleTheme = deleteCaption.getRoleInTheme();
if (capCategory == NvsTimelineCaption.THEME_CATEGORY
&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
deleteCaption = timeline.getNextCaption(deleteCaption);
deleteCaption = timeline.removeCaption(deleteCaption);
NvsTimelineCaption newCaption;
for (CaptionInfo caption : captionArray) {
long duration = caption.getOutPoint() - caption.getInPoint();
newCaption = timeline.addCaption(caption.getText(), caption.getInPoint() + themeDuration,
newCaption = timeline.addModularCaption(caption.getText(), caption.getInPoint() + themeDuration,
```

## `captions-stickers-295` `setCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1405`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `getCategory()`, `e()`, `getRoleInTheme()`, `getNextCaption()`, `removeCaption()`

Simple sequence:

```java
while (deleteCaption != null) {
int capCategory = deleteCaption.getCategory();
int roleTheme = deleteCaption.getRoleInTheme();
if (capCategory == NvsTimelineCaption.THEME_CATEGORY
&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
deleteCaption = timeline.getNextCaption(deleteCaption);
deleteCaption = timeline.removeCaption(deleteCaption);
```

## `captions-stickers-296` `setCompoundCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1443`

API classes: `NvsTimelineCompoundCaption`, `NvsTimeline`
Common calls: `getInPoint()`, `getFirstCompoundCaption()`, `removeCompoundCaption()`, `getOutPoint()`, `addCompoundCaption()`, `getCaptionStyleUuid()`

Simple sequence:

```java
public static boolean setCompoundCaption(NvsTimeline timeline, ArrayList<CompoundCaptionInfo> captionArray) {
if (timeline == null) {
NvsTimelineCompoundCaption deleteCaption = timeline.getFirstCompoundCaption();
while (deleteCaption != null) {
deleteCaption = timeline.removeCompoundCaption(deleteCaption);
for (CompoundCaptionInfo caption : captionArray) {
long duration = caption.getOutPoint() - caption.getInPoint();
NvsTimelineCompoundCaption newCaption = timeline.addCompoundCaption(caption.getInPoint(),
duration, caption.getCaptionStyleUuid());
```

## `captions-stickers-297` `updateCaptionAttribute`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:1540`

API classes: `NvsConstants`, `NvsVideoFx`, `NvsVideoClip`, `NvsTimeline`, `NvsVideoResolution`, `NvsTimelineCaption`, `NvsClipCaption`, `NvsVideoTrack`, `NvsColor`, `NvsStreamingContext`, `NvsSize`, `NvsMaskRegionInfo`
Static/constants: `NvsConstants.CUT_KEY_MASK_GENERATOR_TRANSFORM_2D`, `NvsConstants.KEY_MASK_GENERATOR_TYPE`, `NvsConstants.Crop`, `NvsStreamingContext.getInstance`, `NvsConstants.PROPERTY_KEY_BACKGROUND_MODE`, `NvsConstants.CUT_FX_TYPE_FOR_EXTRA_TRANSFORM`, `NvsConstants.KEY_MASK_GENERATOR`, `NvsConstants.PROPERTY_KEY_SCALE_X`, `NvsConstants.PROPERTY_KEY_SCALE_Y`, `NvsConstants.PROPERTY_KEY_TRANS_X`, `NvsConstants.PROPERTY_KEY_TRANS_Y`, `NvsConstants.CUT_FX_TYPE_FOR_TRANSFORM`
Common calls: `setFloatVal()`, `get()`, `equals()`, `setAttachment()`, `setBooleanVal()`, `removeKeyframeAtTime()`, `setStringVal()`, `getBuiltinVideoFxName()`, `getRawFxByIndex()`, `isEmpty()`, `getInPoint()`, `appendRawBuiltinFx()`

Simple sequence:

```java
public static void updateCaptionAttribute(NvsCaption newCaption, CaptionInfo caption, boolean userRecordingFlag) {
newCaption.setOpacity(caption.getOpacity());
String styleUuid = caption.getCaptionStyleUuid();
newCaption.applyCaptionStyle(styleUuid);
newCaption.applyModularCaptionRenderer(caption.getRichWordUuid());
newCaption.applyModularCaptionContext(caption.getBubbleUuid());
if (!TextUtils.isEmpty(caption.getCombinationAnimationUuid())) {
newCaption.applyModularCaptionAnimation(caption.getCombinationAnimationUuid());
if (caption.getCombinationAnimationDuration() >= 0) {
newCaption.setModularCaptionAnimationPeroid(caption.getCombinationAnimationDuration());
newCaption.applyModularCaptionInAnimation(caption.getMarchInAnimationUuid());
if (newCaption instanceof NvsTimelineCaption) {
inPoint = ((NvsTimelineCaption) newCaption).getInPoint();
outPoint = ((NvsTimelineCaption) newCaption).getOutPoint();
} else if (newCaption instanceof NvsClipCaption) {
inPoint = ((NvsClipCaption) newCaption).getInPoint();
outPoint = ((NvsClipCaption) newCaption).getOutPoint();
if (caption.getMarchInAnimationDuration() >= 0) {
if (maxDuration - caption.getMarchInAnimationDuration() < 500) {
newCaption.setModularCaptionOutAnimationDuration(maxDuration - caption.getMarchInAnimationDuration());
newCaption.setModularCaptionInAnimationDuration(caption.getMarchInAnimationDuration());
newCaption.applyModularCaptionOutAnimation(caption.getMarchOutAnimationUuid());
if (caption.getMarchOutAnimationDuration() >= 0) {
if (maxDuration - caption.getMarchOutAnimationDuration() < 500) {
// ... 461 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-298` `applyMask`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2310`

API classes: `NvsConstants`, `NvsVideoClip`, `NvsVideoFx`
Static/constants: `NvsConstants.KEY_MASK_GENERATOR_TYPE`, `NvsConstants.KEY_MASK_GENERATOR`, `NvsConstants.KEY_MASK_GENERATOR_SIGN_MASK`, `NvsConstants.KEY_MASK_STORYBOARD_DESC`, `NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN`
Common calls: `getMaskType()`, `equals()`, `getFeatherWidth()`, `isReverse()`, `setBooleanVal()`, `setStringVal()`, `setRegionInfo()`, `setArbDataVal()`, `getMaskRegionInfo()`, `getRawFxCount()`, `getRawFxByIndex()`, `getAttachment()`

Simple sequence:

```java
public static void applyMask(NvsVideoClip videoClip, MaskInfoData infoData) {
(infoData.getMaskType() == MaskInfoData.MaskType.NONE ? true : false);
int rawFxCount = videoClip.getRawFxCount();
NvsVideoFx maskFx = null;
for (int i = 0; i < rawFxCount; i++) {
NvsVideoFx fawFx = videoClip.getRawFxByIndex(i);
if (fawFx != null) {
String type = (String) fawFx.getAttachment(NvsConstants.KEY_MASK_GENERATOR_TYPE);
if (TextUtils.equals(fawFx.getBuiltinVideoFxName(), NvsConstants.KEY_MASK_GENERATOR)
&& TextUtils.equals(type, NvsConstants.KEY_MASK_GENERATOR_SIGN_MASK)) {
if (remove) {
videoClip.removeRawFx(i);
videoClip.setImageMotionMode(NvsVideoClip.CLIP_MOTIONMODE_LETTERBOX_ZOOMIN);
videoClip.setImageMotionAnimationEnabled(false);
if (maskFx == null && infoData.getMaskType() != 0) {
maskFx = videoClip.appendRawBuiltinFx(NvsConstants.KEY_MASK_GENERATOR);
maskFx.setAttachment(NvsConstants.KEY_MASK_GENERATOR_TYPE, NvsConstants.KEY_MASK_GENERATOR_SIGN_MASK);
if (maskFx != null) {
maskFx.setFloatVal("Feather Width", infoData.getFeatherWidth());
maskFx.setBooleanVal("Inverse Region", infoData.isReverse());
maskFx.setBooleanVal("Keep RGB", true);
if (infoData.getMaskType() == MaskInfoData.MaskType.TEXT) {
maskFx.setStringVal(NvsConstants.KEY_MASK_STORYBOARD_DESC, infoData.getTextStoryboard());
maskFx.setArbDataVal("Region Info", null);
// ... 2 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-299` `applyClipCaption`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/TimelineUtil.java:2737`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.THEME_CATEGORY`, `NvsTimelineCaption.ROLE_IN_THEME_GENERAL`
Common calls: `getCategory()`, `e()`, `getRoleInTheme()`, `getNextCaption()`, `removeCaption()`

Simple sequence:

```java
while (deleteCaption != null) {
int capCategory = deleteCaption.getCategory();
int roleTheme = deleteCaption.getRoleInTheme();
if (capCategory == NvsTimelineCaption.THEME_CATEGORY
&& roleTheme != NvsTimelineCaption.ROLE_IN_THEME_GENERAL) {
deleteCaption = videoClip.getNextCaption(deleteCaption);
deleteCaption = videoClip.removeCaption(deleteCaption);
```

## `captions-stickers-300` `saveCaptionData`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:482`

API classes: `NvsTimelineCaption`, `NvsClipCaption`, `NvsCaption`
Common calls: `getInPoint()`, `getOutPoint()`, `setInPoint()`, `setOutPoint()`, `setText()`, `getText()`, `setCaptionZVal()`, `getZValue()`, `setCaptionSize()`, `getFontSize()`, `setCaptionColorAlpha()`

Simple sequence:

```java
public static CaptionInfo saveCaptionData(NvsCaption caption) {
if (caption instanceof NvsTimelineCaption) {
inPoint = ((NvsTimelineCaption) caption).getInPoint();
outPoint = ((NvsTimelineCaption) caption).getOutPoint();
} else if (caption instanceof NvsClipCaption) {
inPoint = ((NvsClipCaption) caption).getInPoint();
outPoint = ((NvsClipCaption) caption).getOutPoint();
captionInfo.setInPoint(inPoint);
captionInfo.setOutPoint(outPoint);
captionInfo.setText(caption.getText());
captionInfo.setCaptionZVal((int) caption.getZValue());
captionInfo.setCaptionSize(caption.getFontSize());
captionInfo.setCaptionColorAlpha(100);
```

## `captions-stickers-301` `saveCaptionData`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:486`

API classes: `NvsTimelineCaption`, `NvsClipCaption`
Common calls: `getInPoint()`, `getOutPoint()`

Simple sequence:

```java
if (caption instanceof NvsTimelineCaption) {
inPoint = ((NvsTimelineCaption) caption).getInPoint();
outPoint = ((NvsTimelineCaption) caption).getOutPoint();
} else if (caption instanceof NvsClipCaption) {
inPoint = ((NvsClipCaption) caption).getInPoint();
outPoint = ((NvsClipCaption) caption).getOutPoint();
```

## `captions-stickers-302` `saveCompoundCaptionData`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/Util.java:507`

API classes: `NvsTimelineCompoundCaption`
Common calls: `getInPoint()`, `setInPoint()`, `getOutPoint()`, `setOutPoint()`, `getCaptionCount()`, `addCaptionAttributeList()`, `CompoundCaptionAttr()`, `setCaptionZVal()`, `getZValue()`, `setAnchor()`, `getAnchorPoint()`, `getCaptionTranslation()`

Simple sequence:

```java
public static CompoundCaptionInfo saveCompoundCaptionData(NvsTimelineCompoundCaption caption) {
long inPoint = caption.getInPoint();
captionInfo.setInPoint(inPoint);
long outPoint = caption.getOutPoint();
captionInfo.setOutPoint(outPoint);
int captionCount = caption.getCaptionCount();
captionInfo.setCaptionZVal((int) caption.getZValue());
captionInfo.setAnchor(caption.getAnchorPoint());
PointF pointF = caption.getCaptionTranslation();
captionInfo.setTranslation(pointF);
```

## `captions-stickers-303` `setCaptionBackgroundPadding`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java:785`

API classes: `NvsCaptionSpan`

Simple sequence:

```java
public void setList(List<NvsCaptionSpan> list) {
```

## `captions-stickers-304` `setList`

Source: `app/src/main/java/com/meishe/sdkdemo/utils/dataInfo/CaptionInfo.java:789`

API classes: `NvsCaptionSpan`

Simple sequence:

```java
public List<NvsCaptionSpan> getList() {
```

## `captions-stickers-305` `initTimelineEditor`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:135`

API classes: `NvsMultiThumbnailSequenceView`, `NvsTimelineTimeSpanExt`, `NvsTimelineTimeSpan`
Static/constants: `NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc`, `NvsMultiThumbnailSequenceView.OnScrollChangeListener`
Common calls: `size()`, `scrollTo()`, `addView()`, `mapTimelinePosFromX()`, `getParent()`, `setThumbnailSequenceDescArray()`, `setPixelPerMicrosecond()`, `setStartPadding()`, `setEndPadding()`, `setOnScrollChangeListenser()`, `OnScrollChangeListener()`, `compareTo()`

Simple sequence:

```java
public void initTimelineEditor(ArrayList<NvsMultiThumbnailSequenceView.ThumbnailSequenceDesc> sequenceDesc, final long timelineDuration) {
m_multiThumbnailSequenceView.setThumbnailSequenceDescArray(sequenceDesc);
m_multiThumbnailSequenceView.setPixelPerMicrosecond(m_pixelPerMicrosecond);
m_multiThumbnailSequenceView.setStartPadding(m_sequencLeftPadding);
m_multiThumbnailSequenceView.setEndPadding(m_sequencRightPadding);
m_multiThumbnailSequenceView.setOnScrollChangeListenser(new NvsMultiThumbnailSequenceView.OnScrollChangeListener() {
public void onScrollChanged(NvsMultiThumbnailSequenceView nvsMultiThumbnailSequenceView, int i, int i1) {
if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") == 0) {
NvsTimelineTimeSpan timeSpan = m_timelineTimeSpanArray.get(index);
long inPoint = timeSpan.getInPoint();
long outPoint = timeSpan.getOutPoint();
if (add) {
if (timeSpan.getParent() == null) {
if (timeSpan.getParent() != null) {
m_timeSpanRelativeLayout.removeView(timeSpan);
```

## `captions-stickers-306` `addTimeSpan`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:196`

API classes: `NvsTimelineTimeSpan`
Common calls: `floor()`, `setMinTimeSpanPixel()`, `setMaxTimeSpanPixel()`

Simple sequence:

```java
public NvsTimelineTimeSpan addTimeSpan(long inPoint, long outPoint) {
NvsTimelineTimeSpan timelineTimeSpan = createTimeSpan(inPoint, outPoint);
timelineTimeSpan.setMinTimeSpanPixel(minTimeSpanPixel);
timelineTimeSpan.setMaxTimeSpanPixel(maxTimeSpanPixel);
```

## `captions-stickers-307` `addDouVideoTimeSpan`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:213`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnMarginChangeListener`
Common calls: `floor()`, `setMargins()`, `setBackgroundColor()`, `setBackgroundResource()`, `addRule()`, `addView()`, `getLayoutParams()`, `setLayoutParams()`, `getLeftHandleView()`, `getRightHandleView()`, `getTimeSpanshadowView()`, `setMinTimeSpanPixel()`

Simple sequence:

```java
public NvsTimelineTimeSpan addDouVideoTimeSpan(long inPoint, long outPoint) {
NvsTimelineTimeSpan timelineTimeSpan = createTimeSpan(inPoint, outPoint);
if (timelineTimeSpan != null) {
timelineTimeSpan.getLeftHandleView().setBackgroundResource(R.mipmap.trimline_select_left);
timelineTimeSpan.getRightHandleView().setBackgroundResource(R.mipmap.trimline_select_right);
timelineTimeSpan.getTimeSpanshadowView().setBackgroundColor(Color.TRANSPARENT);
timelineTimeSpan.setMinTimeSpanPixel(minTimeSpanPixel);
timelineTimeSpan.setMaxTimeSpanPixel(maxTimeSpanPixel);
viewLeftMargin.setBackgroundColor(backgrdColor);
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - shadowMarginWidth, 0);
viewRightMargin.setBackgroundColor(backgrdColor);
viewRightMarginParams.setMargins(shadowMarginWidth + spanWidth, 0, 0, 0);
timelineTimeSpan.setMarginChangeListener(new NvsTimelineTimeSpan.OnMarginChangeListener() {
LayoutParams viewLeftMarginParams = (LayoutParams) viewLeftMargin.getLayoutParams();
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - leftMargin, 0);
viewLeftMargin.setLayoutParams(viewLeftMarginParams);
LayoutParams viewRightMarginParams = (LayoutParams) viewRightMargin.getLayoutParams();
viewRightMarginParams.setMargins(leftMargin + timeSpanWidth, 0, 0, 0);
viewRightMargin.setLayoutParams(viewRightMarginParams);
```

## `captions-stickers-308` `addDouVideoTimeSpan`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:215`

API classes: `NvsTimelineTimeSpan`
Static/constants: `NvsTimelineTimeSpan.OnMarginChangeListener`
Common calls: `floor()`, `setMargins()`, `setBackgroundColor()`, `setBackgroundResource()`, `addRule()`, `addView()`, `getLayoutParams()`, `setLayoutParams()`, `getLeftHandleView()`, `getRightHandleView()`, `getTimeSpanshadowView()`, `setMinTimeSpanPixel()`

Simple sequence:

```java
if (timelineTimeSpan != null) {
timelineTimeSpan.getLeftHandleView().setBackgroundResource(R.mipmap.trimline_select_left);
timelineTimeSpan.getRightHandleView().setBackgroundResource(R.mipmap.trimline_select_right);
timelineTimeSpan.getTimeSpanshadowView().setBackgroundColor(Color.TRANSPARENT);
timelineTimeSpan.setMinTimeSpanPixel(minTimeSpanPixel);
timelineTimeSpan.setMaxTimeSpanPixel(maxTimeSpanPixel);
viewLeftMargin.setBackgroundColor(backgrdColor);
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - shadowMarginWidth, 0);
viewRightMargin.setBackgroundColor(backgrdColor);
viewRightMarginParams.setMargins(shadowMarginWidth + spanWidth, 0, 0, 0);
timelineTimeSpan.setMarginChangeListener(new NvsTimelineTimeSpan.OnMarginChangeListener() {
LayoutParams viewLeftMarginParams = (LayoutParams) viewLeftMargin.getLayoutParams();
viewLeftMarginParams.setMargins(0, 0, tmpTotalWidth - leftMargin, 0);
viewLeftMargin.setLayoutParams(viewLeftMarginParams);
LayoutParams viewRightMarginParams = (LayoutParams) viewRightMargin.getLayoutParams();
viewRightMarginParams.setMargins(leftMargin + timeSpanWidth, 0, 0, 0);
viewRightMargin.setLayoutParams(viewRightMarginParams);
```

## `captions-stickers-309` `addTimeSpanExt`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:274`

API classes: `NvsTimelineTimeSpanExt`
Static/constants: `NvsTimelineTimeSpanExt.OnMarginChangeListener`
Common calls: `setMargins()`, `setLayoutParams()`, `addView()`, `floor()`, `setBackgroundColor()`, `addRule()`, `getLayoutParams()`, `compareTo()`, `setMultiThumbnailSequenceView()`, `setInPoint()`, `setOutPoint()`, `setPixelPerMicrosecond()`

Simple sequence:

```java
public NvsTimelineTimeSpanExt addTimeSpanExt(long inPoint, long outPoint) {
if (m_timeSpanType.compareTo("NvsTimelineTimeSpanExt") != 0)
NvsTimelineTimeSpanExt timeSpanExt = new NvsTimelineTimeSpanExt(m_context);
timeSpanExt.setMultiThumbnailSequenceView(m_multiThumbnailSequenceView);
timeSpanExt.setInPoint(inPoint);
timeSpanExt.setOutPoint(outPoint);
timeSpanExt.setPixelPerMicrosecond(m_pixelPerMicrosecond);
int lLeftHandleWidth = timeSpanExt.getLLeftHandleWidth();
timeSpanExt.setTotalWidth(totalWidth);
spanItemParams.setMargins(leftMargin, LayoutParams.MATCH_PARENT, totalWidth - (leftMargin + spanWidth), 0);
timeSpanExt.setLayoutParams(spanItemParams);
viewLeftMargin.setBackgroundColor(backgrdColor);
int tmpMarginHeight = timeSpanExt.getLTopHandleHeight();
viewLeftMarginParams.setMargins(tmpLLeftHandleWidth, 0, tmpTotalWidth - tmpLLeftHandleWidth - leftMargin, 0);
viewRightMargin.setBackgroundColor(backgrdColor);
viewRightMarginParams.setMargins(leftMargin + spanWidth - lLeftHandleWidth, 0, lLeftHandleWidth, 0);
timeSpanExt.setMarginChangeListener(new NvsTimelineTimeSpanExt.OnMarginChangeListener() {
LayoutParams viewLeftMarginParams = (LayoutParams) viewLeftMargin.getLayoutParams();
viewLeftMarginParams.setMargins(tmpLLeftHandleWidth, 0, tmpTotalWidth - leftMargin, 0);
viewLeftMargin.setLayoutParams(viewLeftMarginParams);
LayoutParams viewRightMarginParams = (LayoutParams) viewRightMargin.getLayoutParams();
viewRightMarginParams.setMargins(leftMargin + timeSpanWidth, 0, tmpLLeftHandleWidth, 0);
viewRightMargin.setLayoutParams(viewRightMarginParams);
```

## `captions-stickers-310` `selectTimeSpan`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:445`

API classes: `NvsTimelineTimeSpan`
Common calls: `setHasSelected()`, `requestLayout()`, `bringToFront()`

Simple sequence:

```java
public void selectTimeSpan(NvsTimelineTimeSpan timeSpan) {
timeSpan.setHasSelected(true);
```

## `captions-stickers-311` `timeSpanCount`

Source: `libBase/src/main/java/com/meishe/base/view/NvsTimelineEditor.java:464`

API classes: `NvsTimelineTimeSpan`
Common calls: `getChildCount()`, `removeView()`, `remove()`

Simple sequence:

```java
public void deleteSelectedTimeSpan(NvsTimelineTimeSpan timeSpan) {
int count = m_timeSpanRelativeLayout.getChildCount();
if (count > 0) {
m_timeSpanRelativeLayout.removeView(timeSpan);
```

## `captions-stickers-312` `moveAndRemoveNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:452`

API classes: `NvsTimelineCaption`
Common calls: `isEmpty()`, `size()`, `get()`, `isAICaption()`, `setInPoint()`, `getInPoint()`, `setOutPoint()`, `getOutPoint()`, `getObject()`, `removeCaption()`, `setObject()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setInPoint(clipInfo.getInPoint() + offset);
clipInfo.setOutPoint(clipInfo.getOutPoint() + offset);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
mTimeline.removeCaption((NvsTimelineCaption) object);
clipInfo.setObject(null);
```

## `captions-stickers-313` `moveAndRemoveNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:453`

API classes: `NvsTimelineCaption`
Common calls: `isEmpty()`, `size()`, `get()`, `isAICaption()`, `setInPoint()`, `getInPoint()`, `setOutPoint()`, `getOutPoint()`, `getObject()`, `removeCaption()`, `setObject()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setInPoint(clipInfo.getInPoint() + offset);
clipInfo.setOutPoint(clipInfo.getOutPoint() + offset);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
mTimeline.removeCaption((NvsTimelineCaption) object);
clipInfo.setObject(null);
```

## `captions-stickers-314` `moveAndRemoveNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:454`

API classes: `NvsTimelineCaption`
Common calls: `size()`, `get()`, `isAICaption()`, `setInPoint()`, `getInPoint()`, `setOutPoint()`, `getOutPoint()`, `getObject()`, `removeCaption()`, `setObject()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setInPoint(clipInfo.getInPoint() + offset);
clipInfo.setOutPoint(clipInfo.getOutPoint() + offset);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
mTimeline.removeCaption((NvsTimelineCaption) object);
clipInfo.setObject(null);
```

## `captions-stickers-315` `moveAndRemoveNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:456`

API classes: `NvsTimelineCaption`
Common calls: `isAICaption()`, `setInPoint()`, `getInPoint()`, `setOutPoint()`, `getOutPoint()`, `getObject()`, `removeCaption()`, `setObject()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setInPoint(clipInfo.getInPoint() + offset);
clipInfo.setOutPoint(clipInfo.getOutPoint() + offset);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
mTimeline.removeCaption((NvsTimelineCaption) object);
clipInfo.setObject(null);
```

## `captions-stickers-316` `addNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:469`

API classes: `NvsTimelineCaption`
Common calls: `isEmpty()`, `size()`, `get()`, `isAICaption()`, `getzValue()`, `bindToTimeline()`, `e()`, `setZValue()`, `setBold()`, `setObject()`

Simple sequence:

```java
NvsTimelineCaption caption = ((MeicamCaptionClip) clipInfo).bindToTimeline(mTimeline, false, true);
caption.setZValue(trackIndex);
caption.setBold(false);
((MeicamCaptionClip) clipInfo).setObject(caption);
```

## `captions-stickers-317` `addNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:470`

API classes: `NvsTimelineCaption`
Common calls: `isEmpty()`, `size()`, `get()`, `isAICaption()`, `getzValue()`, `bindToTimeline()`, `e()`, `setZValue()`, `setBold()`, `setObject()`

Simple sequence:

```java
NvsTimelineCaption caption = ((MeicamCaptionClip) clipInfo).bindToTimeline(mTimeline, false, true);
caption.setZValue(trackIndex);
caption.setBold(false);
((MeicamCaptionClip) clipInfo).setObject(caption);
```

## `captions-stickers-318` `addNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:471`

API classes: `NvsTimelineCaption`
Common calls: `size()`, `get()`, `isAICaption()`, `getzValue()`, `bindToTimeline()`, `e()`, `setZValue()`, `setBold()`, `setObject()`

Simple sequence:

```java
NvsTimelineCaption caption = ((MeicamCaptionClip) clipInfo).bindToTimeline(mTimeline, false, true);
caption.setZValue(trackIndex);
caption.setBold(false);
((MeicamCaptionClip) clipInfo).setObject(caption);
```

## `captions-stickers-319` `addNvsCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:473`

API classes: `NvsTimelineCaption`
Common calls: `isAICaption()`, `getzValue()`, `bindToTimeline()`, `e()`, `setZValue()`, `setBold()`, `setObject()`

Simple sequence:

```java
NvsTimelineCaption caption = ((MeicamCaptionClip) clipInfo).bindToTimeline(mTimeline, false, true);
caption.setZValue(trackIndex);
caption.setBold(false);
((MeicamCaptionClip) clipInfo).setObject(caption);
```

## `captions-stickers-320` `changeAICaptionInPoint`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:511`

API classes: `NvsTimelineCaption`
Common calls: `isAICaption()`, `setInPoint()`, `getObject()`, `changeInPoint()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setInPoint(inPoint);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
((NvsTimelineCaption) object).changeInPoint(inPoint);
```

## `captions-stickers-321` `changeAICaptionInPoint`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:512`

API classes: `NvsTimelineCaption`
Common calls: `isAICaption()`, `setInPoint()`, `getObject()`, `changeInPoint()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setInPoint(inPoint);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
((NvsTimelineCaption) object).changeInPoint(inPoint);
```

## `captions-stickers-322` `changeAICaptionInPoint`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:515`

API classes: `NvsTimelineCaption`
Common calls: `changeInPoint()`

Simple sequence:

```java
if (object instanceof NvsTimelineCaption) {
((NvsTimelineCaption) object).changeInPoint(inPoint);
```

## `captions-stickers-323` `changeAICaptionOutPoint`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:527`

API classes: `NvsTimelineCaption`
Common calls: `isAICaption()`, `setOutPoint()`, `getObject()`, `changeOutPoint()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setOutPoint(outPoint);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
((NvsTimelineCaption) object).changeOutPoint(outPoint);
```

## `captions-stickers-324` `changeAICaptionOutPoint`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:528`

API classes: `NvsTimelineCaption`
Common calls: `isAICaption()`, `setOutPoint()`, `getObject()`, `changeOutPoint()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
clipInfo.setOutPoint(outPoint);
Object object = clipInfo.getObject();
if (object instanceof NvsTimelineCaption) {
((NvsTimelineCaption) object).changeOutPoint(outPoint);
```

## `captions-stickers-325` `changeAICaptionOutPoint`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:531`

API classes: `NvsTimelineCaption`
Common calls: `changeOutPoint()`

Simple sequence:

```java
if (object instanceof NvsTimelineCaption) {
((NvsTimelineCaption) object).changeOutPoint(outPoint);
```

## `captions-stickers-326` `addAnimatorSticker`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:622`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getTimelineCurrentPosition()`, `getInstance()`, `getTitleThemeDuration()`, `setInPoint()`, `setOutPoint()`, `setIsCustomSticker()`, `setCoverImagePath()`, `getInPoint()`, `getOutPoint()`, `d()`, `setzValue()`, `bindToTimeline()`

Simple sequence:

```java
long inPoint = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long titleThemeDuration = TimelineData.getInstance().getTitleThemeDuration();
stickerClip.setInPoint(inPoint);
stickerClip.setOutPoint(outPoint);
stickerClip.setIsCustomSticker(false);
stickerClip.setCoverImagePath(coverPath);
int trackIndex = getTrackIndex(stickerClip.getInPoint(), stickerClip.getOutPoint());
stickerClip.bindToTimeline(mTimeline);
seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-327` `addCustomAnimatorSticker`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:721`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getTimelineCurrentPosition()`, `getInstance()`, `getTitleThemeDuration()`, `setInPoint()`, `setOutPoint()`, `setIsCustomSticker()`, `setCustomanimatedStickerImagePath()`, `setCoverImagePath()`, `getInPoint()`, `getOutPoint()`, `d()`, `setzValue()`

Simple sequence:

```java
long inPoint = mStreamingContext.getTimelineCurrentPosition(mTimeline);
long titleThemeDuration = TimelineData.getInstance().getTitleThemeDuration();
stickerClip.setInPoint(inPoint);
stickerClip.setOutPoint(outPoint);
stickerClip.setIsCustomSticker(true);
stickerClip.setCustomanimatedStickerImagePath(filePath);
stickerClip.setCoverImagePath(coverPath);
int trackIndex = getTrackIndex(stickerClip.getInPoint(), stickerClip.getOutPoint());
stickerClip.bindToTimeline(mTimeline);
seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-328` `setCompoundCaptionFont`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:935`

API classes: `NvsStreamingContext`, `NvsTimelineCompoundCaption`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFontFamily()`, `isEmpty()`, `registerFontByFilePath()`

Simple sequence:

```java
public String setCompoundCaptionFont(NvsTimelineCompoundCaption caption, int captionIndex, String fftPath) {
String fontName = mStreamingContext.registerFontByFilePath(fontAssetPath);
caption.setFontFamily(captionIndex, fontName);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
caption.setFontFamily(captionIndex, fftPath);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-329` `setCompoundCaptionFont`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:936`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFontFamily()`, `isEmpty()`, `registerFontByFilePath()`

Simple sequence:

```java
String fontName = mStreamingContext.registerFontByFilePath(fontAssetPath);
caption.setFontFamily(captionIndex, fontName);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
caption.setFontFamily(captionIndex, fftPath);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-330` `seekTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:973`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME`
Common calls: `seekTimeline()`

Simple sequence:

```java
if (useFaceShape) {
flag = NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_BUDDY_HOST_VIDEO_FRAME;
if (seekShowMode > 0) {
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag | seekShowMode
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-331` `seekTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:978`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`, `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `seekTimeline()`

Simple sequence:

```java
if (seekShowMode > 0) {
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag | seekShowMode
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
mStreamingContext.seekTimeline(mTimeline, timestamp, NvsStreamingContext.VIDEO_PREVIEW_SIZEMODE_LIVEWINDOW_SIZE, flag
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER
| NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-332` `addCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1241`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setOperationType()`, `setInPoint()`, `setOutPoint()`, `getInPoint()`, `getOutPoint()`, `setzValue()`, `bindToTimeline()`, `e()`, `setZValue()`, `setBold()`, `setObject()`, `addStickerCaption()`

Simple sequence:

```java
meicamCaptionClip.setOperationType(operateType);
meicamCaptionClip.setInPoint(inPoint);
meicamCaptionClip.setOutPoint(outPoint);
int trackIndex = getTrackIndex(meicamCaptionClip.getInPoint(), meicamCaptionClip.getOutPoint());
NvsTimelineCaption caption = meicamCaptionClip.bindToTimeline(mTimeline, false, isIdentify);
caption.setZValue(trackIndex);
caption.setBold(false);
meicamCaptionClip.setObject(caption);
seekTimeline(inPoint, NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-333` `updateCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1270`

API classes: `NvsTimelineCaption`
Static/constants: `NvsTimelineCaption.ROLE_IN_THEME_TITLE`
Common calls: `getZValue()`, `getInPoint()`, `onAddStickerCaptionPicFx()`, `getInstance()`, `isEmpty()`, `removeStickerCaption()`, `removeCaption()`, `isAddTitleTheme()`, `getRoleInTheme()`, `getMeicamTheme()`, `setThemeTitleText()`, `setText()`

Simple sequence:

```java
if (TextUtils.isEmpty(content)) {
boolean success = TimelineDataUtil.removeStickerCaption((int) caption.getZValue(), caption.getInPoint());
if (success) {
mTimeline.removeCaption(caption);
if (TimelineData.getInstance().isAddTitleTheme() && caption.getRoleInTheme() == NvsTimelineCaption.ROLE_IN_THEME_TITLE) {
TimelineData.getInstance().getMeicamTheme().setThemeTitleText(content);
caption.setText(content);
ClipInfo stickerCaptionData = TimelineDataUtil.getStickerCaptionData((int) caption.getZValue(), caption.getInPoint());
```

## `captions-stickers-334` `removeCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1459`

API classes: `NvsTimelineCaption`
Common calls: `getInPoint()`, `getNextCaption()`, `removeCaption()`, `getFirstCaption()`, `getOutPoint()`

Simple sequence:

```java
NvsTimelineCaption caption = mTimeline.getFirstCaption();
NvsTimelineCaption nextCaption;
while (caption != null) {
if ((start >= caption.getInPoint() && start <= caption.getOutPoint())
|| (caption.getInPoint() >= start && caption.getInPoint() < end)) {
nextCaption = mTimeline.getNextCaption(caption);
TimelineDataUtil.removeCaption(caption.getInPoint());
mTimeline.removeCaption(caption);
caption = mTimeline.getNextCaption(caption);
```

## `captions-stickers-335` `removeAllAICaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1480`

API classes: `NvsTimelineCaption`
Common calls: `removeCaption()`, `getAllAICaption()`, `isEmpty()`, `size()`, `get()`, `isAICaption()`, `getInPoint()`, `getObject()`

Simple sequence:

```java
List<ClipInfo<?>> allAICaption = TimelineDataUtil.getAllAICaption();
if (TimelineDataUtil.isAICaption(clipInfo)) {
TimelineDataUtil.removeCaption(clipInfo.getInPoint());
mTimeline.removeCaption((NvsTimelineCaption) clipInfo.getObject());
```

## `captions-stickers-336` `removeAllAICaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1485`

API classes: `NvsTimelineCaption`
Common calls: `removeCaption()`, `size()`, `get()`, `isAICaption()`, `getInPoint()`, `getObject()`

Simple sequence:

```java
if (TimelineDataUtil.isAICaption(clipInfo)) {
TimelineDataUtil.removeCaption(clipInfo.getInPoint());
mTimeline.removeCaption((NvsTimelineCaption) clipInfo.getObject());
```

## `captions-stickers-337` `removeCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1503`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getInPoint()`, `d()`, `getzValue()`, `getObject()`, `removeStickerCaption()`, `getZValue()`, `e()`, `removeCaption()`, `onAddStickerCaptionPicFx()`, `getTimelineCurrentPosition()`, `onTimelineChanged()`, `onChangeBottomView()`

Simple sequence:

```java
LogUtils.d("removeCaption: " + captionInfo.getzValue() + " " + captionInfo.getInPoint());
NvsTimelineCaption curCaption = captionInfo.getObject();
boolean success = TimelineDataUtil.removeStickerCaption((int) curCaption.getZValue(), curCaption.getInPoint());
mTimeline.removeCaption(curCaption);
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (mOnTimelineChangeListener != null) {
mOnTimelineChangeListener.onTimelineChanged(mTimeline, true);
```

## `captions-stickers-338` `handleCaptionColorConner`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1555`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setBackgroundAngle()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setBackgroundAngle(radius);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-339` `handleCaptionBackgroundColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1572`

API classes: `NvsTimelineCaption`, `NvsColor`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setBackgroundColor()`, `getObject()`, `getBackgroundColor()`, `getColorArray()`, `onSaveOperation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
NvsColor textColor = curCaption.getBackgroundColor();
curCaption.setBackgroundColor(textColor);
meicamCaptionClip.setBackgroundColor(ColorUtil.getColorArray(textColor));
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-340` `handleCaptionOutlineWidth`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1599`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setOutlineWidth()`, `getObject()`, `setDrawOutline()`, `onSaveOperation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
curCaption.setDrawOutline(true);
curCaption.setOutlineWidth(progress / 10F);
meicamCaptionClip.setOutlineWidth(progress / 10F);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-341` `handleCaptionOutLineColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1623`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getOutlineColor()`, `setOutlineColor()`, `onSaveOperation()`

Simple sequence:

```java
float[] outlineColor = meicamCaptionClip.getOutlineColor();
meicamCaptionClip.setOutlineColor(outlineColor);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-342` `handleCaptionTextColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1645`

API classes: `NvsTimelineCaption`, `NvsColor`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setTextColor()`, `getObject()`, `getTextColor()`, `getColorArray()`, `onSaveOperation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
NvsColor textColor = curCaption.getTextColor();
curCaption.setTextColor(textColor);
meicamCaptionClip.setTextColor(ColorUtil.getColorArray(textColor));
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-343` `handleCaptionFont`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1672`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setFontFamily()`, `setFont()`, `getObject()`, `isEmpty()`, `registerFontByFilePath()`, `onSaveOperation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
String fontName = mStreamingContext.registerFontByFilePath(fontAssetPath);
curCaption.setFontFamily(fontName);
meicamCaptionClip.setFont(fontName);
curCaption.setFontFamily(content);
meicamCaptionClip.setFont(content);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-344` `handleCaptionShadow`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1702`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setShadow()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setShadow(hasShadow);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-345` `handleCaptionItalics`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1720`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setItalic()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setItalic(isItalic);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-346` `handleCaptionBold`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1738`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setBold()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setBold(isBold);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-347` `setCaptionLetterSpace`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1756`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getObject()`, `setLetterSpacing()`, `onSaveOperation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
meicamCaptionClip.setLetterSpacing(space);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-348` `setCaptionLineSpace`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1777`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getObject()`, `setLineSpacing()`, `onSaveOperation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
meicamCaptionClip.setLineSpacing(space);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-349` `handleCaptionPosition`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1798`

API classes: `NvsTimelineCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `get()`, `getBoundingRectangleVertices()`, `size()`, `sort()`, `getVideoRes()`, `setTranslationX()`, `getTranslationX()`, `setTranslationY()`, `getTranslationY()`, `getObject()`, `onSaveOperation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
if (intValue == CAPTION_ALIGN_LEFT) {
list = curCaption.getBoundingRectangleVertices();
xOffset = -(mTimeline.getVideoRes().imageWidth / 2f + list.get(0).x);
meicamCaptionClip.setTranslationX(meicamCaptionClip.getTranslationX() + xOffset);
list = curCaption.getBoundingRectangleVertices();
meicamCaptionClip.setTranslationX(meicamCaptionClip.getTranslationX() + xOffset);
list = curCaption.getBoundingRectangleVertices();
xOffset = mTimeline.getVideoRes().imageWidth / 2f - list.get(3).x;
meicamCaptionClip.setTranslationX(meicamCaptionClip.getTranslationX() + xOffset);
list = curCaption.getBoundingRectangleVertices();
yOffset = mTimeline.getVideoRes().imageHeight / 2f - list.get(0).y - y_dis;
meicamCaptionClip.setTranslationY(meicamCaptionClip.getTranslationY() + yOffset);
list = curCaption.getBoundingRectangleVertices();
meicamCaptionClip.setTranslationY(meicamCaptionClip.getTranslationY() + yOffset);
list = curCaption.getBoundingRectangleVertices();
yOffset = -(mTimeline.getVideoRes().imageHeight / 2f + list.get(3).y - y_dis);
meicamCaptionClip.setTranslationY(meicamCaptionClip.getTranslationY() + yOffset);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-350` `handleCaptionAnimationCombination`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1915`

API classes: `NvsTimelineCaption`
Common calls: `isEmpty()`, `getModularCaptionAnimationPeroid()`, `getObject()`, `getModularCaptionOutAnimationPackageId()`, `applyModularCaptionOutAnimation()`, `setModularCaptionOutAnimationDuration()`, `getModularCaptionInAnimationPackageId()`, `applyModularCaptionInAnimation()`, `setModularCaptionInAnimationDuration()`, `setModularCaptionAnimationPeroid()`, `applyModularCaptionAnimation()`, `d()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
if (!TextUtils.isEmpty(curCaption.getModularCaptionOutAnimationPackageId())) {
curCaption.applyModularCaptionOutAnimation("");
curCaption.setModularCaptionOutAnimationDuration(IN_OUT_ANIMATION_DEFAULT_DURATION);
if (!TextUtils.isEmpty(curCaption.getModularCaptionInAnimationPackageId())) {
curCaption.applyModularCaptionInAnimation("");
curCaption.setModularCaptionInAnimationDuration(IN_OUT_ANIMATION_DEFAULT_DURATION);
if (curCaption.getModularCaptionAnimationPeroid() == 0) {
curCaption.setModularCaptionAnimationPeroid(ANIMATION_DEFAULT_DURATION);
boolean isSuccess = curCaption.applyModularCaptionAnimation(uuid);
meicamCaptionClip.setCombinationAnimationUuid(uuid);
meicamCaptionClip.setCombinationAnimationDuration(curCaption.getModularCaptionAnimationPeroid());
meicamCaptionClip.setMarchOutAnimationUuid("");
meicamCaptionClip.setMarchInAnimationUuid("");
playVideo(meicamCaptionClip.getInPoint(), meicamCaptionClip.getOutPoint());
```

## `captions-stickers-351` `handleCaptionAnimationOut`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:1963`

API classes: `NvsTimelineCaption`
Common calls: `isEmpty()`, `getModularCaptionOutAnimationDuration()`, `setMarchOutAnimationDuration()`, `getObject()`, `getModularCaptionAnimationPackageId()`, `applyModularCaptionAnimation()`, `setModularCaptionAnimationPeroid()`, `setModularCaptionOutAnimationDuration()`, `applyModularCaptionOutAnimation()`, `d()`, `setCombinationAnimationUuid()`, `setCombinationAnimationDuration()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
if (!TextUtils.isEmpty(curCaption.getModularCaptionAnimationPackageId())) {
curCaption.applyModularCaptionAnimation("");
curCaption.setModularCaptionAnimationPeroid(ANIMATION_DEFAULT_DURATION);
if (curCaption.getModularCaptionOutAnimationDuration() == 0) {
curCaption.setModularCaptionOutAnimationDuration(IN_OUT_ANIMATION_DEFAULT_DURATION);
boolean isSuccess = curCaption.applyModularCaptionOutAnimation(uuid);
meicamCaptionClip.setCombinationAnimationUuid("");
meicamCaptionClip.setCombinationAnimationDuration(0);
meicamCaptionClip.setMarchOutAnimationUuid(uuid);
meicamCaptionClip.setMarchOutAnimationDuration(curCaption.getModularCaptionOutAnimationDuration());
if (TextUtils.isEmpty(uuid)) {
meicamCaptionClip.setMarchOutAnimationDuration(0);
playVideo(meicamCaptionClip.getInPoint(), meicamCaptionClip.getOutPoint());
```

## `captions-stickers-352` `handleCaptionAnimationIn`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2006`

API classes: `NvsTimelineCaption`
Common calls: `isEmpty()`, `getModularCaptionInAnimationDuration()`, `isModular()`, `setMarchInAnimationDuration()`, `getObject()`, `getModularCaptionAnimationPackageId()`, `applyModularCaptionAnimation()`, `setModularCaptionAnimationPeroid()`, `setModularCaptionInAnimationDuration()`, `applyModularCaptionInAnimation()`, `d()`, `setCombinationAnimationUuid()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
if (!TextUtils.isEmpty(curCaption.getModularCaptionAnimationPackageId())) {
curCaption.applyModularCaptionAnimation("");
curCaption.setModularCaptionAnimationPeroid(ANIMATION_DEFAULT_DURATION);
if (curCaption.getModularCaptionInAnimationDuration() == 0) {
curCaption.setModularCaptionInAnimationDuration(IN_OUT_ANIMATION_DEFAULT_DURATION);
boolean isSuccess = curCaption.applyModularCaptionInAnimation(uuid);
meicamCaptionClip.setCombinationAnimationUuid("");
meicamCaptionClip.setCombinationAnimationDuration(0);
meicamCaptionClip.setMarchInAnimationUuid(uuid);
meicamCaptionClip.setMarchInAnimationDuration(curCaption.getModularCaptionInAnimationDuration());
if (TextUtils.isEmpty(uuid)) {
meicamCaptionClip.setMarchInAnimationDuration(0);
playVideo(meicamCaptionClip.getInPoint(), meicamCaptionClip.getOutPoint());
```

## `captions-stickers-353` `deleteSticker`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2046`

API classes: `NvsTimelineAnimatedSticker`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `getObject()`, `getZValue()`, `removeAnimatedSticker()`, `removeStickerCaption()`, `getInPoint()`, `getTimelineCurrentPosition()`, `onAddStickerCaptionPicFx()`, `onTimelineChanged()`, `onChangeBottomView()`

Simple sequence:

```java
NvsTimelineAnimatedSticker curAnimateSticker = stickerInfo.getObject();
int zVal = (int) curAnimateSticker.getZValue();
mTimeline.removeAnimatedSticker(curAnimateSticker);
TimelineDataUtil.removeStickerCaption(zVal, stickerInfo.getInPoint());
seekTimeline(mStreamingContext.getTimelineCurrentPosition(mTimeline), NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
if (mOnTimelineChangeListener != null) {
mOnTimelineChangeListener.onTimelineChanged(mTimeline, true);
```

## `captions-stickers-354` `removeCompoundCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2073`

API classes: `NvsTimelineCompoundCaption`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getzValue()`, `getInPoint()`, `d()`, `getObject()`, `removeStickerCaption()`, `removeCompoundCaption()`, `onAddStickerCaptionPicFx()`, `onTimelineChanged()`, `onChangeBottomView()`

Simple sequence:

```java
LogUtils.d("removeCompoundCaption: getzValue: " + meicamCompoundCaptionClip.getzValue() + " getInPoint: " + meicamCompoundCaptionClip.getInPoint());
NvsTimelineCompoundCaption currCompoundCaption = meicamCompoundCaptionClip.getObject();
TimelineDataUtil.removeStickerCaption((int) meicamCompoundCaptionClip.getzValue(), meicamCompoundCaptionClip.getInPoint());
mTimeline.removeCompoundCaption(currCompoundCaption);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (mOnTimelineChangeListener != null) {
mOnTimelineChangeListener.onTimelineChanged(mTimeline, true);
```

## `captions-stickers-355` `copyCaption`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2161`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getInPoint()`, `getOutPoint()`, `clone()`, `setInPoint()`, `setOutPoint()`, `getzValue()`, `setzValue()`, `bindToTimeline()`, `addStickerCaption()`, `onTimelineChanged()`

Simple sequence:

```java
long inPoint = currSelectedCaption.getInPoint();
long captionDuration = currSelectedCaption.getOutPoint() - currSelectedCaption.getInPoint();
meicamCaptionClip.setInPoint(inPoint);
meicamCaptionClip.setOutPoint(outPoint);
int trackIndex = getTrackIndexByCopy(meicamCaptionClip.getInPoint(), meicamCaptionClip.getOutPoint(), (int) meicamCaptionClip.getzValue());
meicamCaptionClip.bindToTimeline(mTimeline);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
if (mOnTimelineChangeListener != null) {
mOnTimelineChangeListener.onTimelineChanged(mTimeline, true);
```

## `captions-stickers-356` `changeStickerVoice`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2392`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `setVolumeGain()`, `setLeftVolume()`, `getObject()`, `getVolumeGain()`

Simple sequence:

```java
NvsTimelineAnimatedSticker sticker = meicamStickerClip.getObject();
if (sticker != null) {
float leftVolume = (int) sticker.getVolumeGain().leftVolume;
if (leftVolume > 0) {
sticker.setVolumeGain(0, 0);
meicamStickerClip.setLeftVolume(0f);
sticker.setVolumeGain(1.0f, 1.0f);
meicamStickerClip.setLeftVolume(1.0f);
```

## `captions-stickers-357` `changeStickerMirror`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2411`

API classes: `NvsTimelineAnimatedSticker`, `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER`
Common calls: `setHorizontalFlip()`, `getObject()`, `getHorizontalFlip()`, `onSaveOperation()`

Simple sequence:

```java
if (mTimeline == null) {
NvsTimelineAnimatedSticker timelineAnimatedSticker = meicamStickerClip.getObject();
boolean isHorizFlip = !timelineAnimatedSticker.getHorizontalFlip();
timelineAnimatedSticker.setHorizontalFlip(isHorizFlip);
meicamStickerClip.setHorizontalFlip(isHorizFlip);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_ANIMATED_STICKER_POSTER);
```

## `captions-stickers-358` `applyCaptionPositionToAll`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2442`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getStickerCaption()`, `isEmpty()`, `getCaptionTranslation()`, `setTranslation()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
List<ClipInfo<?>> clipInfos = TimelineDataUtil.getStickerCaption();
PointF captionTranslation = curCaption.getCaptionTranslation();
if (clipInfo instanceof MeicamCaptionClip) {
((MeicamCaptionClip) clipInfo).setTranslation(captionTranslation);
```

## `captions-stickers-359` `applyCaptionFontToAll`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2469`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getStickerCaption()`, `isEmpty()`, `getFontFamily()`, `setFont()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
List<ClipInfo<?>> clipInfos = TimelineDataUtil.getStickerCaption();
String fontFamily = curCaption.getFontFamily();
if (clipInfo instanceof MeicamCaptionClip) {
((MeicamCaptionClip) clipInfo).setFont(fontFamily);
```

## `captions-stickers-360` `applyCaptionLetterSpaceToAll`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2496`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getStickerCaption()`, `isEmpty()`, `getLetterSpacing()`, `setLetterSpacing()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
List<ClipInfo<?>> clipInfos = TimelineDataUtil.getStickerCaption();
float letterSpacing = curCaption.getLetterSpacing();
if (clipInfo instanceof MeicamCaptionClip) {
((MeicamCaptionClip) clipInfo).setLetterSpacing(letterSpacing);
```

## `captions-stickers-361` `applyCaptionOutlineToAll`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2522`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getStickerCaption()`, `isEmpty()`, `getOutlineColor()`, `setOutlineColor()`

Simple sequence:

```java
NvsTimelineCaption curCaption = meicamCaptionClip.getObject();
List<ClipInfo<?>> clipInfos = TimelineDataUtil.getStickerCaption();
float[] outlineColor = meicamCaptionClip.getOutlineColor();
if (clipInfo instanceof MeicamCaptionClip) {
((MeicamCaptionClip) clipInfo).setOutlineColor(outlineColor);
```

## `captions-stickers-362` `removeCaptionOutlineColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2578`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setOutline()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setOutline(false);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-363` `removeCaptionBackgroundColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2595`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `getBackgroundColor()`, `setBackgroundColor()`, `onSaveOperation()`

Simple sequence:

```java
float[] backgroundColor = meicamCaptionClip.getBackgroundColor();
meicamCaptionClip.setBackgroundColor(backgroundColor);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-364` `removeCaptionBackgroundColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2600`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `setBackgroundColor()`

Simple sequence:

```java
meicamCaptionClip.setBackgroundColor(backgroundColor);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-365` `setCaptionBackgroundColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2616`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `isEmpty()`, `stringColorToColor()`, `setBackgroundColor()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setBackgroundColor(color);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-366` `setCaptionOutLineColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2634`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `isEmpty()`, `stringColorToColor()`, `setOutlineColor()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setOutlineColor(colorArray);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-367` `setCaptionTextColor`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2652`

API classes: `NvsStreamingContext`
Static/constants: `NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER`
Common calls: `isEmpty()`, `stringColorToColor()`, `setTextColor()`, `onSaveOperation()`

Simple sequence:

```java
meicamCaptionClip.setTextColor(colorArray);
seekTimeline(NvsStreamingContext.STREAMING_ENGINE_SEEK_FLAG_SHOW_CAPTION_POSTER);
```

## `captions-stickers-368` `updateCaptionTranslation`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2670`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getCaptionTranslation()`, `setTranslationX()`, `setTranslationY()`

Simple sequence:

```java
if (meicamCaptionClip != null) {
NvsTimelineCaption nvsTimelineCaption = meicamCaptionClip.getObject();
if (nvsTimelineCaption != null) {
PointF captionTranslation = nvsTimelineCaption.getCaptionTranslation();
if (captionTranslation != null) {
meicamCaptionClip.setTranslationX(captionTranslation.x);
meicamCaptionClip.setTranslationY(captionTranslation.y);
```

## `captions-stickers-369` `updateCaptionTranslation`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2671`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getCaptionTranslation()`, `setTranslationX()`, `setTranslationY()`

Simple sequence:

```java
if (meicamCaptionClip != null) {
NvsTimelineCaption nvsTimelineCaption = meicamCaptionClip.getObject();
if (nvsTimelineCaption != null) {
PointF captionTranslation = nvsTimelineCaption.getCaptionTranslation();
if (captionTranslation != null) {
meicamCaptionClip.setTranslationX(captionTranslation.x);
meicamCaptionClip.setTranslationY(captionTranslation.y);
```

## `captions-stickers-370` `updateStickerTranslation`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2688`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `getObject()`, `getTranslation()`, `setTranslationX()`, `setTranslationY()`

Simple sequence:

```java
if (meicamStickerClip != null) {
NvsTimelineAnimatedSticker timelineAnimatedSticker = meicamStickerClip.getObject();
if (timelineAnimatedSticker != null) {
PointF translation = timelineAnimatedSticker.getTranslation();
if (translation != null) {
meicamStickerClip.setTranslationX(translation.x);
meicamStickerClip.setTranslationY(translation.y);
```

## `captions-stickers-371` `updateStickerTranslation`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2689`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `getObject()`, `getTranslation()`, `setTranslationX()`, `setTranslationY()`

Simple sequence:

```java
if (meicamStickerClip != null) {
NvsTimelineAnimatedSticker timelineAnimatedSticker = meicamStickerClip.getObject();
if (timelineAnimatedSticker != null) {
PointF translation = timelineAnimatedSticker.getTranslation();
if (translation != null) {
meicamStickerClip.setTranslationX(translation.x);
meicamStickerClip.setTranslationY(translation.y);
```

## `captions-stickers-372` `updateCompoundCaptionTranslation`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2706`

API classes: `NvsTimelineCompoundCaption`
Common calls: `getObject()`, `getCaptionTranslation()`, `setTranslationX()`, `setTranslationY()`, `setRotation()`, `getRotationZ()`

Simple sequence:

```java
if (meicamCompoundCaptionClip != null) {
NvsTimelineCompoundCaption timelineCompoundCaption = meicamCompoundCaptionClip.getObject();
if (timelineCompoundCaption != null) {
PointF translation = timelineCompoundCaption.getCaptionTranslation();
if (translation != null) {
meicamCompoundCaptionClip.setTranslationX(translation.x);
meicamCompoundCaptionClip.setTranslationY(translation.y);
meicamCompoundCaptionClip.setRotation(timelineCompoundCaption.getRotationZ());
```

## `captions-stickers-373` `updateCompoundCaptionTranslation`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2707`

API classes: `NvsTimelineCompoundCaption`
Common calls: `getObject()`, `getCaptionTranslation()`, `setTranslationX()`, `setTranslationY()`, `setRotation()`, `getRotationZ()`

Simple sequence:

```java
if (meicamCompoundCaptionClip != null) {
NvsTimelineCompoundCaption timelineCompoundCaption = meicamCompoundCaptionClip.getObject();
if (timelineCompoundCaption != null) {
PointF translation = timelineCompoundCaption.getCaptionTranslation();
if (translation != null) {
meicamCompoundCaptionClip.setTranslationX(translation.x);
meicamCompoundCaptionClip.setTranslationY(translation.y);
meicamCompoundCaptionClip.setRotation(timelineCompoundCaption.getRotationZ());
```

## `captions-stickers-374` `updateCaptionScale`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2725`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getScaleX()`, `getScaleY()`, `setScaleX()`, `setScaleY()`, `setRotation()`, `getRotationZ()`

Simple sequence:

```java
if (meicamCaptionClip != null) {
NvsTimelineCaption timelineCaption = meicamCaptionClip.getObject();
if (timelineCaption != null) {
float scaleX = timelineCaption.getScaleX();
float scaleY = timelineCaption.getScaleY();
meicamCaptionClip.setScaleX(scaleX);
meicamCaptionClip.setScaleY(scaleY);
meicamCaptionClip.setRotation(timelineCaption.getRotationZ());
```

## `captions-stickers-375` `updateCaptionScale`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2726`

API classes: `NvsTimelineCaption`
Common calls: `getObject()`, `getScaleX()`, `getScaleY()`, `setScaleX()`, `setScaleY()`, `setRotation()`, `getRotationZ()`

Simple sequence:

```java
if (meicamCaptionClip != null) {
NvsTimelineCaption timelineCaption = meicamCaptionClip.getObject();
if (timelineCaption != null) {
float scaleX = timelineCaption.getScaleX();
float scaleY = timelineCaption.getScaleY();
meicamCaptionClip.setScaleX(scaleX);
meicamCaptionClip.setScaleY(scaleY);
meicamCaptionClip.setRotation(timelineCaption.getRotationZ());
```

## `captions-stickers-376` `updateStickerScale`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2743`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `getObject()`, `getScale()`, `setRotation()`, `getRotationZ()`, `setScale()`

Simple sequence:

```java
if (meicamStickerClip != null) {
NvsTimelineAnimatedSticker timelineAnimatedSticker = meicamStickerClip.getObject();
if (timelineAnimatedSticker != null) {
float scale = timelineAnimatedSticker.getScale();
meicamStickerClip.setRotation(timelineAnimatedSticker.getRotationZ());
meicamStickerClip.setScale(scale);
```

## `captions-stickers-377` `updateStickerScale`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2744`

API classes: `NvsTimelineAnimatedSticker`
Common calls: `getObject()`, `getScale()`, `setRotation()`, `getRotationZ()`, `setScale()`

Simple sequence:

```java
if (meicamStickerClip != null) {
NvsTimelineAnimatedSticker timelineAnimatedSticker = meicamStickerClip.getObject();
if (timelineAnimatedSticker != null) {
float scale = timelineAnimatedSticker.getScale();
meicamStickerClip.setRotation(timelineAnimatedSticker.getRotationZ());
meicamStickerClip.setScale(scale);
```

## `captions-stickers-378` `updateCompoundCaptionScale`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2759`

API classes: `NvsTimelineCompoundCaption`
Common calls: `getObject()`, `getScaleX()`, `getScaleY()`, `setScaleX()`, `setScaleY()`

Simple sequence:

```java
if (meicamCompoundClip != null) {
NvsTimelineCompoundCaption timelineCompoundCaption = meicamCompoundClip.getObject();
if (timelineCompoundCaption != null) {
float scaleX = timelineCompoundCaption.getScaleX();
float scaleY = timelineCompoundCaption.getScaleY();
meicamCompoundClip.setScaleX(scaleX);
meicamCompoundClip.setScaleY(scaleY);
```

## `captions-stickers-379` `updateCompoundCaptionScale`

Source: `libEngine/src/main/java/com/meishe/engine/EditorEngine.java:2760`

API classes: `NvsTimelineCompoundCaption`
Common calls: `getObject()`, `getScaleX()`, `getScaleY()`, `setScaleX()`, `setScaleY()`

Simple sequence:

```java
if (meicamCompoundClip != null) {
NvsTimelineCompoundCaption timelineCompoundCaption = meicamCompoundClip.getObject();
if (timelineCompoundCaption != null) {
float scaleX = timelineCompoundCaption.getScaleX();
float scaleY = timelineCompoundCaption.getScaleY();
meicamCompoundClip.setScaleX(scaleX);
meicamCompoundClip.setScaleY(scaleY);
```

## `captions-stickers-380` `getTranslationX`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:203`

API classes: `NvsTimelineCaption`
Common calls: `setCaptionTranslation()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setCaptionTranslation(new PointF(translationX, getTranslationY()));
```

## `captions-stickers-381` `getTranslationY`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:224`

API classes: `NvsTimelineCaption`
Common calls: `setCaptionTranslation()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setCaptionTranslation(new PointF(getTranslationX(), translationY));
```

## `captions-stickers-382` `getFont`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:236`

API classes: `NvsTimelineCaption`
Common calls: `setFontFamily()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setFontFamily(font);
```

## `captions-stickers-383` `getLineSpacing`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:248`

API classes: `NvsTimelineCaption`
Common calls: `setLineSpacing()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setLineSpacing(lineSpacing);
```

## `captions-stickers-384` `getTextColor`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:260`

API classes: `NvsTimelineCaption`, `NvsColor`
Common calls: `colorFloatToNvsColor()`, `setTextColor()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
NvsColor nvsColor = ColorUtil.colorFloatToNvsColor(textColor);
if (nvsColor != null) {
object.setTextColor(nvsColor);
```

## `captions-stickers-385` `isBold`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:275`

API classes: `NvsTimelineCaption`
Common calls: `setBold()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setBold(bold);
```

## `captions-stickers-386` `isItalic`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:287`

API classes: `NvsTimelineCaption`
Common calls: `setItalic()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setItalic(italic);
```

## `captions-stickers-387` `isShadow`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:299`

API classes: `NvsTimelineCaption`
Common calls: `setDrawShadow()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setDrawShadow(shadow);
```

## `captions-stickers-388` `isOutline`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:311`

API classes: `NvsTimelineCaption`
Common calls: `setDrawOutline()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setDrawOutline(outline);
```

## `captions-stickers-389` `getOutlineColor`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:323`

API classes: `NvsTimelineCaption`, `NvsColor`
Common calls: `colorFloatToNvsColor()`, `setDrawOutline()`, `setOutlineColor()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
NvsColor nvsColor = ColorUtil.colorFloatToNvsColor(outlineColor);
if (nvsColor != null) {
object.setDrawOutline(true);
object.setOutlineColor(nvsColor);
```

## `captions-stickers-390` `getLetterSpacing`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:355`

API classes: `NvsTimelineCaption`
Common calls: `setLetterSpacing()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setLetterSpacing(letterSpacing);
```

## `captions-stickers-391` `getBackgroundColor`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:375`

API classes: `NvsTimelineCaption`, `NvsColor`
Common calls: `colorFloatToNvsColor()`, `setBackgroundColor()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
NvsColor nvsColor = ColorUtil.colorFloatToNvsColor(backgroundColor);
if (nvsColor != null) {
object.setBackgroundColor(nvsColor);
```

## `captions-stickers-392` `getBackgroundAngle`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:390`

API classes: `NvsTimelineCaption`
Common calls: `setBackgroundRadius()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.setBackgroundRadius(backgroundAngle);
```

## `captions-stickers-393` `getRichWordUuid`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:402`

API classes: `NvsTimelineCaption`
Common calls: `applyModularCaptionRenderer()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.applyModularCaptionRenderer(richWordUuid);
```

## `captions-stickers-394` `getBubbleUuid`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:414`

API classes: `NvsTimelineCaption`
Common calls: `applyModularCaptionContext()`

Simple sequence:

```java
NvsTimelineCaption object = getObject();
if (object != null) {
object.applyModularCaptionContext(bubbleUuid);
```

## `captions-stickers-395` `setOperationType`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:479`

API classes: `NvsTimelineCaption`, `NvsTimeline`

Simple sequence:

```java
public NvsTimelineCaption bindToTimeline(NvsTimeline timeline) {
return bindToTimeline(timeline, true, false);
```

## `captions-stickers-396` `bindToTimeline`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:484`

API classes: `NvsTimelineCaption`, `NvsTimeline`, `NvsCaption`, `NvsVideoResolution`
Static/constants: `NvsCaption.LETTER_SPACING_TYPE_ABSOLUTE`
Common calls: `getTextColor()`, `getVideoRes()`, `get()`, `addModularCaption()`, `setClipAffinityEnabled()`, `setLetterSpacingType()`, `e()`, `setScaleX()`, `setScaleY()`, `getBoundingRectangleVertices()`, `size()`, `abs()`

Simple sequence:

```java
public NvsTimelineCaption bindToTimeline(NvsTimeline timeline, boolean isNeedUpdateAttribute, boolean isIdentify) {
NvsTimelineCaption caption = timeline.addModularCaption(getText(), getInPoint(),
caption.setClipAffinityEnabled(false);
Log.e(TAG, "bindToTimeline: " + caption.getTextColor().r + "  " + caption.getTextColor().g + "   " + caption.getTextColor().b + "   "
+ caption.getTextColor().a);
if (isIdentify) {
NvsVideoResolution videoRes = timeline.getVideoRes();
caption.setScaleX(getScaleX());
caption.setScaleY(getScaleY());
List<PointF> list = caption.getBoundingRectangleVertices();
if (list != null && list.size() >= 4) {
y = Math.abs(list.get(1).y - list.get(0).y) / 2 - timeline.getVideoRes().imageHeight / 2f + 40;
```

## `captions-stickers-397` `loadData`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCaptionClip.java:638`

API classes: `NvsColor`, `NvsTimelineCaption`
Common calls: `getInPoint()`, `getOutPoint()`, `getText()`, `getCaptionStylePackageId()`, `getTextColor()`, `getCaptionTranslation()`, `getScaleX()`, `getScaleY()`, `getRotationZ()`, `getLetterSpacing()`, `getLineSpacing()`, `getFontFamily()`

Simple sequence:

```java
public void loadData(NvsTimelineCaption caption) {
setInPoint(caption.getInPoint());
setOutPoint(caption.getOutPoint());
text = caption.getText();
styleId = caption.getCaptionStylePackageId();
NvsColor color = caption.getTextColor();
PointF point = caption.getCaptionTranslation();
scaleX = caption.getScaleX();
scaleY = caption.getScaleY();
rotation = caption.getRotationZ();
letterSpacing = caption.getLetterSpacing();
lineSpacing = caption.getLineSpacing();
font = caption.getFontFamily();
bold = caption.getBold();
italic = caption.getItalic();
shadow = caption.getDrawShadow();
outline = caption.getDrawOutline();
zValue = (int) caption.getZValue();
textAlign = caption.getTextAlignment();
backgroundAngle = caption.getBackgroundRadius();
NvsColor nvsColor = caption.getOutlineColor();
NvsColor nvsBgColor = caption.getBackgroundColor();
outlineWidth = caption.getOutlineWidth();
richWordUuid = caption.getModularCaptionRendererPackageId();
// ... 1 more SDK-related lines omitted in this compressed snippet ...
```

## `captions-stickers-398` `setItemSelectedIndex`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:118`

API classes: `NvsTimelineCompoundCaption`, `NvsColor`
Common calls: `getInPoint()`, `getOutPoint()`, `getCaptionCount()`, `clear()`, `getText()`, `getTextColor()`, `setTextColor()`, `setFont()`, `getFontFamily()`, `add()`, `getCaptionTranslation()`, `getScaleX()`

Simple sequence:

```java
public void loadData(NvsTimelineCompoundCaption comCaption) {
setInPoint(comCaption.getInPoint());
setOutPoint(comCaption.getOutPoint());
int captionCount = comCaption.getCaptionCount();
for (int index = 0; index < captionCount; index++) {
MeicamCompoundCaptionItem meicamCompoundCaptionItem = new MeicamCompoundCaptionItem(index, comCaption.getText(index));
NvsColor color = comCaption.getTextColor(index);
meicamCompoundCaptionItem.setTextColor(textColor);
meicamCompoundCaptionItem.setFont(comCaption.getFontFamily(index));
PointF point = comCaption.getCaptionTranslation();
scaleX = comCaption.getScaleX();
scaleY = comCaption.getScaleY();
rotation = comCaption.getRotationZ();
zValue = comCaption.getZValue();
```

## `captions-stickers-399` `addCompoundCaptionFirst`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamCompoundCaptionClip.java:171`

API classes: `NvsTimelineCompoundCaption`
Common calls: `setZValue()`, `e()`

Simple sequence:

```java
if (mNvsTimelineCompoundCaption != null) {
mNvsTimelineCompoundCaption.setZValue(zValue);
LogUtils.e("addCompoundCaptionFirst", "NvsTimelineCompoundCaption is null! inpoint: "+ getInPoint()
```

## `captions-stickers-400` `getCustomanimatedStickerImagePath`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:147`

API classes: `NvsTimelineAnimatedSticker`, `NvsTimeline`
Common calls: `setHorizontalFlip()`, `addCustomAnimatedSticker()`, `addAnimatedSticker()`, `setClipAffinityEnabled()`, `setScale()`, `setZValue()`, `setRotationZ()`, `setTranslation()`, `setVolumeGain()`, `setVerticalFlip()`

Simple sequence:

```java
public NvsTimelineAnimatedSticker bindToTimeline(NvsTimeline timeline) {
if (timeline == null) {
NvsTimelineAnimatedSticker nvsTimelineAnimatedSticker = isCustomSticker ?
timeline.addCustomAnimatedSticker(getInPoint(), duration, getPackageId(), getCustomanimatedStickerImagePath())
: timeline.addAnimatedSticker(getInPoint(), duration, getPackageId());
nvsTimelineAnimatedSticker.setHorizontalFlip(isHorizontalFlip());
nvsTimelineAnimatedSticker.setClipAffinityEnabled(false);
if (scaleFactor > 0) {
nvsTimelineAnimatedSticker.setScale(scaleFactor);
nvsTimelineAnimatedSticker.setZValue(getzValue());
nvsTimelineAnimatedSticker.setRotationZ(rotation);
nvsTimelineAnimatedSticker.setTranslation(translation);
nvsTimelineAnimatedSticker.setVolumeGain(volumeGain, volumeGain);
nvsTimelineAnimatedSticker.setHorizontalFlip(isHorizontalFlip());
nvsTimelineAnimatedSticker.setVerticalFlip(isVerticalFlip());
```

## `captions-stickers-401` `setzValue`

Source: `libEngine/src/main/java/com/meishe/engine/bean/MeicamStickerClip.java:238`

API classes: `NvsTimeline`, `NvsTimelineAnimatedSticker`
Common calls: `removeAnimatedSticker()`

Simple sequence:

```java
public void removeFromTimeline(NvsTimeline timeline) {
NvsTimelineAnimatedSticker object = getObject();
if (object != null) {
timeline.removeAnimatedSticker(object);
```

## `captions-stickers-402` `LogStickerAndCaption`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1350`

API classes: `NvsTimelineAnimatedSticker`, `NvsTimelineCaption`, `NvsTimelineCompoundCaption`
Common calls: `e()`, `getInPoint()`, `getOutPoint()`, `getzValue()`, `getObject()`, `getZValue()`, `size()`, `get()`, `getInstance()`, `getMeicamStickerCaptionTrackList()`, `getClipInfoList()`

Simple sequence:

```java
List<MeicamStickerCaptionTrack> meicamStickerCaptionTrackList = TimelineData.getInstance().getMeicamStickerCaptionTrackList();
List<ClipInfo<?>> clipInfoList = meicamStickerCaptionTrack.getClipInfoList();
Log.e(TAG, "LogStickerAndCaption:贴纸: trackIndex: " + i + " getInPoint: " + meicamStickerClip.getInPoint() + "  getOutPoint: " + meicamStickerClip.getOutPoint() + " getzValue: " + meicamStickerClip.getzValue());
NvsTimelineAnimatedSticker animatedSticker = meicamStickerClip.getObject();
Log.e(TAG, "LogStickerAndCaption:贴纸: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
Log.e(TAG, "LogStickerAndCaption:字幕: trackIndex: " + i + " getInPoint: " + meicamCaptionClip.getInPoint() + "  getOutPoint: " + meicamCaptionClip.getOutPoint() + " getzValue: " + meicamCaptionClip.getzValue());
NvsTimelineCaption animatedSticker = meicamCaptionClip.getObject();
Log.e(TAG, "LogStickerAndCaption:字幕: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
Log.e(TAG, "LogStickerAndCaption:组合字幕: trackIndex: " + i + " getInPoint: " + meicamCompoundCaptionClip.getInPoint() + "  getOutPoint: " + meicamCompoundCaptionClip.getOutPoint() + " getzValue: " + meicamCompoundCaptionClip.getzValue());
NvsTimelineCompoundCaption animatedSticker = meicamCompoundCaptionClip.getObject();
Log.e(TAG, "LogStickerAndCaption:组合字幕: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
```

## `captions-stickers-403` `LogStickerAndCaption`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1352`

API classes: `NvsTimelineAnimatedSticker`, `NvsTimelineCaption`, `NvsTimelineCompoundCaption`
Common calls: `e()`, `getInPoint()`, `getOutPoint()`, `getzValue()`, `getObject()`, `getZValue()`, `size()`, `get()`, `getClipInfoList()`

Simple sequence:

```java
List<ClipInfo<?>> clipInfoList = meicamStickerCaptionTrack.getClipInfoList();
Log.e(TAG, "LogStickerAndCaption:贴纸: trackIndex: " + i + " getInPoint: " + meicamStickerClip.getInPoint() + "  getOutPoint: " + meicamStickerClip.getOutPoint() + " getzValue: " + meicamStickerClip.getzValue());
NvsTimelineAnimatedSticker animatedSticker = meicamStickerClip.getObject();
Log.e(TAG, "LogStickerAndCaption:贴纸: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
Log.e(TAG, "LogStickerAndCaption:字幕: trackIndex: " + i + " getInPoint: " + meicamCaptionClip.getInPoint() + "  getOutPoint: " + meicamCaptionClip.getOutPoint() + " getzValue: " + meicamCaptionClip.getzValue());
NvsTimelineCaption animatedSticker = meicamCaptionClip.getObject();
Log.e(TAG, "LogStickerAndCaption:字幕: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
Log.e(TAG, "LogStickerAndCaption:组合字幕: trackIndex: " + i + " getInPoint: " + meicamCompoundCaptionClip.getInPoint() + "  getOutPoint: " + meicamCompoundCaptionClip.getOutPoint() + " getzValue: " + meicamCompoundCaptionClip.getzValue());
NvsTimelineCompoundCaption animatedSticker = meicamCompoundCaptionClip.getObject();
Log.e(TAG, "LogStickerAndCaption:组合字幕: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
```

## `captions-stickers-404` `LogStickerAndCaption`

Source: `libEngine/src/main/java/com/meishe/engine/bean/TimelineDataUtil.java:1355`

API classes: `NvsTimelineAnimatedSticker`, `NvsTimelineCaption`, `NvsTimelineCompoundCaption`
Common calls: `e()`, `getInPoint()`, `getOutPoint()`, `getzValue()`, `getObject()`, `getZValue()`, `size()`, `get()`

Simple sequence:

```java
Log.e(TAG, "LogStickerAndCaption:贴纸: trackIndex: " + i + " getInPoint: " + meicamStickerClip.getInPoint() + "  getOutPoint: " + meicamStickerClip.getOutPoint() + " getzValue: " + meicamStickerClip.getzValue());
NvsTimelineAnimatedSticker animatedSticker = meicamStickerClip.getObject();
Log.e(TAG, "LogStickerAndCaption:贴纸: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
Log.e(TAG, "LogStickerAndCaption:字幕: trackIndex: " + i + " getInPoint: " + meicamCaptionClip.getInPoint() + "  getOutPoint: " + meicamCaptionClip.getOutPoint() + " getzValue: " + meicamCaptionClip.getzValue());
NvsTimelineCaption animatedSticker = meicamCaptionClip.getObject();
Log.e(TAG, "LogStickerAndCaption:字幕: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
Log.e(TAG, "LogStickerAndCaption:组合字幕: trackIndex: " + i + " getInPoint: " + meicamCompoundCaptionClip.getInPoint() + "  getOutPoint: " + meicamCompoundCaptionClip.getOutPoint() + " getzValue: " + meicamCompoundCaptionClip.getzValue());
NvsTimelineCompoundCaption animatedSticker = meicamCompoundCaptionClip.getObject();
Log.e(TAG, "LogStickerAndCaption:组合字幕: trackIndex: " + i + " getInPoint: " + animatedSticker.getInPoint() + "  getOutPoint: " + animatedSticker.getOutPoint() + " getzValue: " + animatedSticker.getZValue());
```

## `captions-stickers-405` `getCaptionByAttachment`

Source: `libEngine/src/main/java/com/meishe/engine/editor/EditorController.java:1233`

API classes: `NvsTimelineCaption`
Common calls: `e()`, `getFirstCaption()`

Simple sequence:

```java
public NvsTimelineCaption getCaptionByAttachment(String replaceId) {
NvsTimelineCaption nextCaption = mNvsTimeline.getFirstCaption();
```

## `captions-stickers-406` `setItemSelectedIndex`

Source: `libEngine/src/main/java/com/meishe/engine/local/LMeicamCompoundCaptionClip.java:114`

API classes: `NvsTimelineCompoundCaption`, `NvsColor`
Common calls: `isEmpty()`, `getCompoundCaptionItems()`, `getCaptionCount()`, `get()`, `colorFloatToNvsColor()`, `getTextColor()`, `setTextColor()`, `getFont()`, `setFontFamily()`, `getText()`, `setText()`, `getScaleX()`

Simple sequence:

```java
private static void updateCompoundCaptionAttribute(NvsTimelineCompoundCaption newCaption, LMeicamCompoundCaptionClip meicamCompoundCaptionClip) {
List<LMeicamCompoundCaptionItem> captionAttrList = meicamCompoundCaptionClip.getCompoundCaptionItems();
int captionCount = newCaption.getCaptionCount();
NvsColor textColor = ColorUtil.colorFloatToNvsColor(compoundCaptionItem.getTextColor());
newCaption.setTextColor(index, textColor);
String fontName = compoundCaptionItem.getFont();
if (!TextUtils.isEmpty(fontName)) {
newCaption.setFontFamily(index, fontName);
String captionText = compoundCaptionItem.getText();
if (!TextUtils.isEmpty(captionText)) {
newCaption.setText(index, captionText);
float scaleFactorX = meicamCompoundCaptionClip.getScaleX();
float scaleFactorY = meicamCompoundCaptionClip.getScaleY();
newCaption.setScaleX(scaleFactorX);
newCaption.setScaleY(scaleFactorY);
float rotation = meicamCompoundCaptionClip.getRotation();
newCaption.setRotationZ(rotation);
newCaption.setZValue(meicamCompoundCaptionClip.getzValue());
PointF translation = new PointF(meicamCompoundCaptionClip.getTranslationX(), meicamCompoundCaptionClip.getTranslationY());
newCaption.setCaptionTranslation(translation);
```

## `captions-stickers-407` `setSitckerCaptionObject`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:374`

API classes: `NvsTimeline`
Common calls: `bindToTimeline()`, `getInstance()`, `getMeicamStickerCaptionTrackList()`, `getClipInfoList()`

Simple sequence:

```java
public static void setSitckerCaptionObject(NvsTimeline timeline) {
List<MeicamStickerCaptionTrack> meicamStickerCaptionTrackList = TimelineData.getInstance().getMeicamStickerCaptionTrackList();
for (MeicamStickerCaptionTrack meicamStickerCaptionTrack : meicamStickerCaptionTrackList) {
List<ClipInfo<?>> clipInfoList = meicamStickerCaptionTrack.getClipInfoList();
meicamStickerClip.bindToTimeline(timeline);
meicamCaptionClip.bindToTimeline(timeline);
meicamCompoundCaptionClip.bindToTimeline(timeline);
```

## `captions-stickers-408` `removeAllSticker`

Source: `libEngine/src/main/java/com/meishe/engine/util/TimelineUtil.java:393`

API classes: `NvsTimeline`, `NvsTimelineAnimatedSticker`
Common calls: `e()`, `getFirstAnimatedSticker()`, `removeAnimatedSticker()`

Simple sequence:

```java
private static void removeAllSticker(NvsTimeline timeline) {
if (timeline == null) {
Log.e(TAG, "removeAllSticker: timeline is null");
NvsTimelineAnimatedSticker sticker = timeline.getFirstAnimatedSticker();
while (sticker != null) {
sticker = timeline.removeAnimatedSticker(sticker);
```
