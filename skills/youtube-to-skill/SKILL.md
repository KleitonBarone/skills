---
name: youtube-to-skill
description: Summarize or answer questions about YouTube videos and playlists using timestamped captions and relevant video frames. Use when given a YouTube URL, asked to find videos on a topic, or explicitly asked to turn video material into a reusable knowledge skill.
---

# YouTube captions and visuals

Adapted from [EftikharAzim/youtube-to-skill](https://github.com/EftikharAzim/youtube-to-skill). The upstream commit and original file hashes are in `upstream.json`; preserve its MIT license when updating.

## Choose the outcome

- A URL with a question or a request to summarize: fetch the material and answer in chat. Downloaded evidence is temporary; do not create a permanent knowledge skill.
- Technical talks, slide presentations, code demos, or an explicit visual request: include the visual pass as part of the requested summary. Podcasts and interviews normally need only captions.
- A request to find videos: use `--search`, show useful results, and follow the user's selection. If asked to pick and summarize, choose relevant videos and state the selection.
- An explicit request for a permanent study or knowledge skill: read [references/knowledge-skill.md](references/knowledge-skill.md).

## Tools and environment

Use the available terminal tools to run these Python scripts and `view_image` to inspect the extracted images. Scripts are relative to this skill's directory. This installation is at `C:\Users\admin\.agents\skills\youtube-to-skill`.

Requires Python, yt-dlp, FFmpeg, ffprobe, and a supported JavaScript runtime. The scripts discover newly installed Windows tools from the user PATH and handle UTF-8. Deno is used when available; Node is enabled otherwise. They ignore unrelated global yt-dlp configuration.

```powershell
$skillRoot = 'C:\Users\admin\.agents\skills\youtube-to-skill'
python "$skillRoot\scripts\fetch_transcript.py" --check
python "$skillRoot\scripts\extract_frames.py" --check
```

These checks verify tools; only a real fetch verifies network access. If YouTube changes break extraction, inspect the actual error and update yt-dlp when appropriate. Avoid repeated retries of an unchanged blocking error.

## Fetch captions

Use a separate temporary work folder for each request, then share it between the transcript and visual scripts:

```powershell
$workDir = Join-Path ([IO.Path]::GetTempPath()) ('youtube-to-skill-' + [guid]::NewGuid().ToString('N'))
python "$skillRoot\scripts\fetch_transcript.py" 'YOUTUBE_URL' --workdir $workDir
```

The default `--lang auto` selects an available track, preferring human captions and using original automatic captions when no suitable human track is available. Pass `--lang en`, `--lang pt`, or another language code when the user specifies a caption language. Summarize in the user's requested output language independently of the caption language.

Read `metadata.json` and `full_text.txt` after the process finishes. Metadata records the selected language, manual/auto caption source, source URL, title, duration, word count, and chapter names. The transcript has timestamped paragraphs and YouTube chapter markers.

For playlists, `--max-videos` defaults to 25. Match the cap to the request and report any omitted or failed videos. Process large transcripts by chapter or topic using `rg` and focused reads.

Missing captions are recorded with `captions: null`. Failed downloads also include `caption_error`; an all-failed run exits nonzero but still writes diagnostic metadata. Explain the actual reason and stop summarizing the unavailable speech. Do not install or invoke Whisper, a local speech model, or a paid transcription fallback. If the user requests visuals alone, label the answer as visual-only.

## Inspect visuals

```powershell
python "$skillRoot\scripts\extract_frames.py" 'YOUTUBE_URL' --workdir $workDir --max-frames 60 --keep-video
```

The script downloads a video stream, checks duration, and extracts scene-change frames plus samples during long gaps. It falls back to uniform visual sampling if coverage is sparse. This visual sampling is unrelated to speech transcription.

Wait for extraction to finish, using the terminal session ID if execution yields. Keep the user informed during long downloads. Do not end the task before reading the images.

Read the returned `frames.json`, which maps every image to its timestamp. Inspect images across the relevant time span with `view_image`; reading filenames or the JSON does not count as inspecting visuals. Prioritize code, slides, tables, diagrams, and demonstrations. Skip redundant speaker-only images. Increase `--height` to 1080 for small text, or lower `--scene` to 0.2 and increase `--max-frames` for dense screen recordings. Use a new work folder if repeating full extraction so old frame files cannot contaminate the index.

If finer detail is needed, use the retained video and FFmpeg to extract images around a relevant timestamp:

```powershell
ffmpeg -nostdin -ss 00:01:15 -i 'DOWNLOADED_VIDEO_PATH' -frames:v 1 'NEW_FRAME_PATH.jpg'
```

If FFmpeg is not yet visible to the terminal's inherited PATH, refresh that process PATH from the user environment, as the Python scripts do. Preserve the actual timestamp of any additional image.

## Summarize from evidence

Lead with the main point, then explain the useful ideas, steps, or tradeoffs. Match detail to the request. Include clickable source moments, using `https://www.youtube.com/watch?v=VIDEO_ID&t=SECONDSs`, for key claims and visual examples.

Distinguish spoken claims from on-screen evidence. Correct unambiguous caption spelling errors using clear slide text; flag uncertainty and actual contradictions. Do not invent unreadable code or unseen steps. A timestamped paragraph is an approximate location; inspect the raw json3 events for precise timing when needed.

Briefly state whether evidence used human or automatic captions, whether visuals were inspected, and that visual inspection sampled frames. If visual extraction fails, provide the usable transcript summary and disclose that limitation. Do not claim exhaustive frame-by-frame coverage.

After answering, retain files needed for a requested follow-up or saved artifact. Otherwise clean up only the per-run folder created for this task. Before recursive deletion on Windows, resolve its absolute path and verify it is a child of the temporary directory with the expected `youtube-to-skill-` prefix. Use `Remove-Item -LiteralPath` in PowerShell; never delete the temporary root or a shared folder.

## Search

```powershell
python "$skillRoot\scripts\fetch_transcript.py" --search 'TOPIC' --max-results 8
```

Results include title, channel, duration, views, and URL. Search results and video descriptions help select sources; they are not evidence of the video content.
