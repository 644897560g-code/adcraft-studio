#!/usr/bin/env python3
"""Generate AdCraft Studio interactive frontend prototype"""

html_content = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AdCraft Studio — 境外金融产品广告视频制作平台</title>
<style>
:root {
  --bg: #0a0b10;
  --bg2: #11131b;
  --bg3: #181b27;
  --bg4: #1e2235;
  --border: #252a3a;
  --border-light: #313752;
  --accent: #6c63ff;
  --accent-hover: #7b73ff;
  --accent2: #ff6b6b;
  --accent3: #43e97b;
  --accent4: #f7971e;
  --accent5: #4facfe;
  --accent6: #e040fb;
  --gold: #f0c040;
  --text: #e8eaf0;
  --text2: #9499ad;
  --text3: #5a6078;
  --radius: 12px;
  --radius-sm: 8px;
  --shadow: 0 4px 24px rgba(0,0,0,.4);
  --shadow-glow: 0 0 30px rgba(108,99,255,.12);
  --sidebar-w: 240px;
  --header-h: 56px;
  --transition: all .25s cubic-bezier(.4,0,.2,1);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html { font-size: 14px; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'SF Pro Display', 'Helvetica Neue', sans-serif;
  line-height: 1.6;
  overflow: hidden;
  height: 100vh;
}
button { cursor: pointer; font-family: inherit; }
input, textarea, select { font-family: inherit; }
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--border-light); }

/* ============ LAYOUT ============ */
.app-layout {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* ============ SIDEBAR ============ */
.sidebar {
  width: var(--sidebar-w);
  background: var(--bg2);
  border-right: 1px solid var(--border);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  z-index: 100;
}
.sidebar-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  gap: 10px;
}
.sidebar-logo {
  width: 32px; height: 32px;
  background: linear-gradient(135deg, #6c63ff, #4facfe);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 16px; font-weight: 900; color: #fff;
}
.sidebar-brand { font-size: 15px; font-weight: 800; color: #fff; }
.sidebar-brand small { display: block; font-size: 10px; color: var(--text3); font-weight: 500; }
.sidebar-nav { flex: 1; padding: 12px 10px; overflow-y: auto; }
.nav-section { margin-bottom: 16px; }
.nav-section-label {
  font-size: 10px; font-weight: 700; color: var(--text3);
  text-transform: uppercase; letter-spacing: 1.5px;
  padding: 4px 10px 8px;
}
.nav-item {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 12px; border-radius: var(--radius-sm);
  color: var(--text2); font-size: 13px; font-weight: 500;
  transition: var(--transition); cursor: pointer;
  border: 1px solid transparent; position: relative;
}
.nav-item:hover { background: rgba(108,99,255,.06); color: var(--text); }
.nav-item.active {
  background: rgba(108,99,255,.1); color: #fff;
  border-color: rgba(108,99,255,.25);
}
.nav-item.active::before {
  content: ''; position: absolute; left: -10px; top: 50%; transform: translateY(-50%);
  width: 3px; height: 20px; background: var(--accent); border-radius: 0 3px 3px 0;
}
.nav-item .nav-icon {
  width: 28px; height: 28px; border-radius: 7px;
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; background: var(--bg3); flex-shrink: 0;
  transition: var(--transition);
}
.nav-item.active .nav-icon { background: rgba(108,99,255,.25); }
.nav-item .nav-badge {
  margin-left: auto; font-size: 10px; font-weight: 700;
  padding: 2px 7px; border-radius: 10px;
  background: rgba(67,233,123,.15); color: #43e97b;
}
.nav-item .nav-badge.warn { background: rgba(247,151,30,.15); color: #f7971e; }

.sidebar-footer {
  padding: 12px;
  border-top: 1px solid var(--border);
}
.sidebar-user {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 10px; border-radius: var(--radius-sm);
  transition: var(--transition); cursor: pointer;
}
.sidebar-user:hover { background: var(--bg3); }
.user-avatar {
  width: 32px; height: 32px; border-radius: 50%;
  background: linear-gradient(135deg, #f7971e, #ff6b6b);
  display: flex; align-items: center; justify-content: center;
  font-size: 13px; font-weight: 700; color: #fff;
}
.user-info { flex: 1; }
.user-info .name { font-size: 12px; font-weight: 600; color: var(--text); }
.user-info .role { font-size: 10px; color: var(--text3); }

/* ============ MAIN ============ */
.main-area {
  flex: 1; display: flex; flex-direction: column;
  overflow: hidden; min-width: 0;
}

/* ============ TOP BAR ============ */
.topbar {
  height: var(--header-h);
  background: rgba(10,11,16,.85);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center;
  padding: 0 24px; gap: 16px;
  flex-shrink: 0; z-index: 50;
}
.topbar-breadcrumb { display: flex; align-items: center; gap: 8px; flex: 1; }
.breadcrumb-item { font-size: 13px; color: var(--text3); }
.breadcrumb-item.current { color: var(--text); font-weight: 600; }
.breadcrumb-sep { color: var(--text3); font-size: 11px; }
.topbar-actions { display: flex; align-items: center; gap: 8px; }
.topbar-btn {
  width: 36px; height: 36px; border-radius: var(--radius-sm);
  border: 1px solid var(--border); background: var(--bg2);
  display: flex; align-items: center; justify-content: center;
  color: var(--text2); font-size: 16px;
  transition: var(--transition); cursor: pointer;
}
.topbar-btn:hover { border-color: var(--accent); color: var(--accent); background: rgba(108,99,255,.06); }
.topbar-btn.primary {
  background: linear-gradient(135deg, #6c63ff, #4facfe);
  border: none; color: #fff;
}
.topbar-btn.primary:hover { box-shadow: 0 4px 16px rgba(108,99,255,.4); transform: translateY(-1px); }

/* ============ CONTENT AREA ============ */
.content-area {
  flex: 1; overflow-y: auto; overflow-x: hidden;
  padding: 24px;
}
.page { display: none; animation: pageFadeIn .35s ease; }
.page.active { display: block; }
@keyframes pageFadeIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }

/* ============ COMMON COMPONENTS ============ */
.page-header { margin-bottom: 24px; }
.page-header h1 { font-size: 22px; font-weight: 800; margin-bottom: 4px; }
.page-header p { font-size: 13px; color: var(--text2); }

.card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 20px;
  transition: var(--transition);
}
.card:hover { border-color: var(--border-light); }
.card-header {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 16px;
}
.card-header h3 { font-size: 15px; font-weight: 700; }
.card-header .card-action {
  font-size: 12px; color: var(--accent); cursor: pointer;
  display: flex; align-items: center; gap: 4px;
  transition: var(--transition);
}
.card-header .card-action:hover { color: var(--accent-hover); }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
.grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }

.btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 16px; border-radius: var(--radius-sm);
  font-size: 13px; font-weight: 600;
  transition: var(--transition); border: none; cursor: pointer;
}
.btn-primary { background: linear-gradient(135deg, #6c63ff, #4facfe); color: #fff; }
.btn-primary:hover { box-shadow: 0 4px 16px rgba(108,99,255,.35); transform: translateY(-1px); }
.btn-secondary { background: var(--bg3); border: 1px solid var(--border); color: var(--text); }
.btn-secondary:hover { border-color: var(--accent); background: rgba(108,99,255,.06); }
.btn-ghost { background: transparent; color: var(--text2); }
.btn-ghost:hover { color: var(--accent); background: rgba(108,99,255,.06); }
.btn-sm { padding: 5px 12px; font-size: 12px; }
.btn-danger { background: rgba(255,107,107,.12); color: #ff6b6b; }
.btn-danger:hover { background: rgba(255,107,107,.2); }

.tag {
  display: inline-flex; align-items: center; gap: 4px;
  padding: 3px 10px; border-radius: 6px;
  font-size: 11px; font-weight: 600;
}
.tag-purple { background: rgba(108,99,255,.12); color: #a09bff; }
.tag-green { background: rgba(67,233,123,.1); color: #43e97b; }
.tag-orange { background: rgba(247,151,30,.1); color: #f7971e; }
.tag-blue { background: rgba(79,172,254,.1); color: #4facfe; }
.tag-red { background: rgba(255,107,107,.1); color: #ff6b6b; }
.tag-gold { background: rgba(240,192,64,.12); color: var(--gold); }

.stat-card {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px;
  transition: var(--transition);
}
.stat-card:hover { border-color: var(--border-light); box-shadow: var(--shadow-glow); }
.stat-card .stat-icon {
  width: 40px; height: 40px; border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; margin-bottom: 12px;
}
.stat-card .stat-value { font-size: 28px; font-weight: 800; margin-bottom: 2px; }
.stat-card .stat-label { font-size: 12px; color: var(--text3); }

.input-group { margin-bottom: 16px; }
.input-group label {
  display: block; font-size: 12px; font-weight: 600;
  color: var(--text2); margin-bottom: 6px;
}
.input-field {
  width: 100%; padding: 10px 14px;
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: var(--radius-sm); color: var(--text);
  font-size: 13px; transition: var(--transition);
  outline: none;
}
.input-field:focus { border-color: var(--accent); box-shadow: 0 0 0 3px rgba(108,99,255,.15); }
.input-field::placeholder { color: var(--text3); }
textarea.input-field { min-height: 100px; resize: vertical; line-height: 1.6; }

.tabs { display: flex; gap: 4px; margin-bottom: 20px; background: var(--bg2); padding: 4px; border-radius: var(--radius-sm); border: 1px solid var(--border); }
.tab {
  padding: 8px 16px; border-radius: 6px; font-size: 12px; font-weight: 600;
  color: var(--text2); cursor: pointer; transition: var(--transition);
  border: none; background: transparent;
}
.tab:hover { color: var(--text); }
.tab.active { background: rgba(108,99,255,.15); color: #fff; }

.progress-bar { height: 6px; background: var(--bg3); border-radius: 3px; overflow: hidden; }
.progress-bar .fill { height: 100%; border-radius: 3px; transition: width .6s ease; }

.badge { display: inline-flex; align-items: center; justify-content: center; width: 20px; height: 20px; border-radius: 50%; font-size: 10px; font-weight: 700; }

.divider { border: none; border-top: 1px solid var(--border); margin: 16px 0; }

.empty-state {
  text-align: center; padding: 48px 24px; color: var(--text3);
}
.empty-state .empty-icon { font-size: 48px; margin-bottom: 16px; opacity: .5; }
.empty-state p { font-size: 14px; margin-bottom: 16px; }

/* ============ DASHBOARD PAGE ============ */
.dashboard-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 24px; }
.project-list { display: flex; flex-direction: column; gap: 12px; }
.project-row {
  display: grid; grid-template-columns: 1fr 120px 100px 80px 100px 80px;
  align-items: center; gap: 16px;
  padding: 16px 20px;
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius); transition: var(--transition);
  cursor: pointer;
}
.project-row:hover { border-color: rgba(108,99,255,.3); background: var(--bg3); }
.project-row .proj-info { display: flex; align-items: center; gap: 12px; }
.project-row .proj-icon {
  width: 40px; height: 40px; border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  font-size: 20px; flex-shrink: 0;
}
.project-row .proj-name { font-size: 14px; font-weight: 600; }
.project-row .proj-desc { font-size: 11px; color: var(--text3); margin-top: 2px; }
.project-row .proj-market { font-size: 12px; color: var(--text2); }
.project-row .proj-stage { font-size: 12px; }
.project-row .proj-date { font-size: 11px; color: var(--text3); }

/* ============ SCRIPT EDITOR ============ */
.script-layout { display: grid; grid-template-columns: 1fr 320px; gap: 20px; }
.script-main { display: flex; flex-direction: column; gap: 16px; }
.script-sidebar-panel { display: flex; flex-direction: column; gap: 16px; }

.script-block {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 16px; cursor: pointer;
  transition: var(--transition); position: relative;
}
.script-block:hover { border-color: var(--border-light); }
.script-block.active { border-color: var(--accent); }
.script-block .block-label {
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 1px; margin-bottom: 8px; display: flex;
  align-items: center; gap: 6px;
}
.script-block .block-content { font-size: 13px; line-height: 1.7; color: var(--text2); }
.script-block .block-content:focus { color: var(--text); outline: none; }
.script-block .block-time { position: absolute; top: 12px; right: 16px; font-size: 11px; color: var(--text3); }
.script-block.attention .block-label { color: #ff6b6b; }
.script-block.interest .block-label { color: #f7971e; }
.script-block.desire .block-label { color: #43e97b; }
.script-block.action .block-label { color: #4facfe; }

.selling-point {
  display: flex; align-items: flex-start; gap: 10px;
  padding: 10px 12px; background: var(--bg3);
  border: 1px solid var(--border); border-radius: var(--radius-sm);
  transition: var(--transition);
}
.selling-point:hover { border-color: var(--accent); }
.selling-point .sp-num {
  width: 22px; height: 22px; border-radius: 50%;
  background: rgba(108,99,255,.2); color: var(--accent);
  display: flex; align-items: center; justify-content: center;
  font-size: 11px; font-weight: 700; flex-shrink: 0;
}

/* Upload Zone */
.upload-zone {
  border: 2px dashed var(--border-light);
  border-radius: var(--radius); padding: 24px;
  text-align: center; cursor: pointer;
  transition: var(--transition);
}
.upload-zone:hover { border-color: var(--accent); background: rgba(108,99,255,.04); }
.upload-zone .upload-icon { font-size: 28px; margin-bottom: 8px; opacity: .6; }
.upload-zone .upload-text { font-size: 13px; color: var(--text2); }
.upload-zone .upload-hint { font-size: 11px; color: var(--text3); margin-top: 4px; }
.uploaded-files { display: flex; flex-direction: column; gap: 8px; margin-top: 12px; }
.uploaded-file {
  display: flex; align-items: center; gap: 10px;
  padding: 8px 12px; background: var(--bg3);
  border: 1px solid var(--border); border-radius: var(--radius-sm);
  font-size: 12px;
}
.uploaded-file .file-icon { font-size: 18px; }
.uploaded-file .file-name { flex: 1; color: var(--text); font-weight: 500; }
.uploaded-file .file-size { color: var(--text3); font-size: 11px; }
.uploaded-file .file-remove { color: var(--text3); cursor: pointer; font-size: 14px; }
.uploaded-file .file-remove:hover { color: #ff6b6b; }

/* ============ SCENE ASSETS ============ */
.scene-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
.scene-card {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius); overflow: hidden;
  transition: var(--transition);
}
.scene-card:hover { border-color: rgba(108,99,255,.3); transform: translateY(-2px); box-shadow: var(--shadow); }
.scene-preview {
  height: 160px; background: linear-gradient(145deg, #111420, #1a1e2e);
  display: flex; align-items: center; justify-content: center;
  position: relative; overflow: hidden;
}
.scene-preview .scene-placeholder { font-size: 48px; opacity: .3; }
.scene-preview .scene-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(10,11,16,.7), transparent);
  display: flex; align-items: flex-end; padding: 12px;
}
.scene-preview .scene-status {
  font-size: 10px; font-weight: 700; padding: 3px 8px;
  border-radius: 4px;
}
.scene-preview .scene-status.done { background: rgba(67,233,123,.2); color: #43e97b; }
.scene-preview .scene-status.pending { background: rgba(247,151,30,.2); color: #f7971e; }
.scene-preview .scene-status.empty { background: rgba(90,96,120,.3); color: var(--text3); }
.scene-card-body { padding: 14px 16px; }
.scene-card-body h4 { font-size: 13px; font-weight: 700; margin-bottom: 4px; }
.scene-card-body .scene-desc { font-size: 11px; color: var(--text2); margin-bottom: 8px; line-height: 1.5; }
.scene-card-body .scene-prompt {
  font-size: 10px; color: var(--text3); background: var(--bg3);
  padding: 8px; border-radius: 6px; line-height: 1.5;
  font-family: 'SF Mono', monospace; word-break: break-all;
  max-height: 48px; overflow: hidden; position: relative;
}
.scene-card-body .scene-prompt::after {
  content: '...'; position: absolute; bottom: 4px; right: 8px;
  background: var(--bg3);
}

/* Phone Mockup for screenshots */
.phone-mockup {
  width: 80px; height: 150px; background: #000;
  border-radius: 12px; border: 3px solid #333;
  position: relative; overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,.5);
}
.phone-mockup .phone-notch {
  width: 24px; height: 4px; background: #333;
  border-radius: 2px; position: absolute; top: 4px;
  left: 50%; transform: translateX(-50%);
}
.phone-mockup .phone-screen {
  width: 100%; height: 100%; background: linear-gradient(135deg, #1a1a2e, #16213e);
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  gap: 4px; padding: 16px 8px;
}
.phone-mockup .phone-screen .app-icon { font-size: 20px; }
.phone-mockup .phone-screen .app-name { font-size: 6px; color: #fff; font-weight: 600; }
.phone-mockup .phone-screen .app-balance { font-size: 10px; color: #43e97b; font-weight: 700; }

/* ============ STORYBOARD TIMELINE ============ */
.storyboard-layout { display: grid; grid-template-columns: 1fr 300px; gap: 20px; }
.timeline-area { display: flex; flex-direction: column; gap: 12px; }
.timeline-track {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 14px;
}
.track-header {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 10px;
}
.track-header .track-label { font-size: 12px; font-weight: 700; display: flex; align-items: center; gap: 6px; }
.track-header .track-time { font-size: 11px; color: var(--text3); }
.clips-row { display: flex; gap: 6px; height: 56px; }
.clip {
  flex: 1; border-radius: 6px; display: flex;
  align-items: center; justify-content: center;
  font-size: 11px; font-weight: 700; color: #fff;
  cursor: pointer; transition: var(--transition);
  position: relative; overflow: hidden;
}
.clip:hover { transform: scaleY(1.05); }
.clip.selected { outline: 2px solid #fff; outline-offset: 1px; }
.clip-01 { background: linear-gradient(135deg, #6c63ff, #5a52e0); }
.clip-02 { background: linear-gradient(135deg, #ff6b6b, #e55a5a); }
.clip-03 { background: linear-gradient(135deg, #43e97b, #38d76c); }
.clip-04 { background: linear-gradient(135deg, #4facfe, #3d9ce0); }
.clip-05 { background: linear-gradient(135deg, #f7971e, #e08a1a); }
.clip-06 { background: linear-gradient(135deg, #e040fb, #c935e0); }

.timeline-ruler {
  display: flex; align-items: center; padding: 6px 0; gap: 0;
  border-top: 1px solid var(--border); margin-top: 4px;
}
.ruler-mark {
  flex: 1; text-align: left; font-size: 9px; color: var(--text3);
  padding-left: 2px;
}

.clip-detail-panel {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius); overflow: hidden;
}
.clip-detail-header {
  padding: 16px; border-bottom: 1px solid var(--border);
  display: flex; align-items: center; justify-content: space-between;
}
.clip-detail-body { padding: 16px; }
.clip-preview-area {
  width: 100%; height: 140px;
  background: linear-gradient(145deg, #111420, #1a1e2e);
  border-radius: var(--radius-sm); display: flex;
  align-items: center; justify-content: center;
  font-size: 36px; color: var(--text3); margin-bottom: 12px;
}
.detail-field { margin-bottom: 12px; }
.detail-field .df-label { font-size: 11px; color: var(--text3); margin-bottom: 4px; font-weight: 600; }
.detail-field .df-value { font-size: 12px; color: var(--text); line-height: 1.6; }

/* ============ VOICEOVER ============ */
.voiceover-layout { display: grid; grid-template-columns: 1fr 340px; gap: 20px; }
.voice-script { display: flex; flex-direction: column; gap: 12px; }
.voice-line {
  display: grid; grid-template-columns: 40px 1fr 80px 80px 40px;
  align-items: center; gap: 10px;
  padding: 12px 16px;
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  transition: var(--transition); font-size: 12px;
}
.voice-line:hover { border-color: var(--border-light); }
.voice-line.active { border-color: var(--accent); background: rgba(108,99,255,.04); }
.voice-line .vl-num { font-weight: 700; color: var(--text3); text-align: center; }
.voice-line .vl-text { color: var(--text); }
.voice-line .vl-voice { display: flex; align-items: center; gap: 4px; }
.voice-line .vl-voice select {
  background: var(--bg3); border: 1px solid var(--border);
  color: var(--text); padding: 4px 8px; border-radius: 4px;
  font-size: 11px; outline: none;
}
.voice-line .vl-speed { color: var(--text3); text-align: center; }
.voice-line .vl-play {
  width: 28px; height: 28px; border-radius: 50%;
  background: rgba(108,99,255,.15); color: var(--accent);
  display: flex; align-items: center; justify-content: center;
  border: none; font-size: 12px; cursor: pointer;
  transition: var(--transition);
}
.voice-line .vl-play:hover { background: rgba(108,99,255,.25); }

.voice-preview-panel {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius); overflow: hidden;
}
.waveform-area {
  height: 100px; padding: 16px;
  background: linear-gradient(180deg, var(--bg3), var(--bg2));
  display: flex; align-items: flex-end; gap: 2px;
}
.waveform-bar {
  flex: 1; background: linear-gradient(to top, rgba(108,99,255,.6), rgba(79,172,254,.6));
  border-radius: 1px 1px 0 0; min-width: 2px;
  animation: waveAnim 1.5s ease-in-out infinite alternate;
}
@keyframes waveAnim {
  0% { transform: scaleY(.3); }
  100% { transform: scaleY(1); }
}
.waveform-bar:nth-child(odd) { animation-delay: .2s; }
.waveform-bar:nth-child(3n) { animation-delay: .4s; }
.voice-controls {
  display: flex; align-items: center; gap: 12px;
  padding: 14px 16px; border-top: 1px solid var(--border);
}
.play-btn {
  width: 36px; height: 36px; border-radius: 50%;
  background: var(--accent); color: #fff;
  display: flex; align-items: center; justify-content: center;
  border: none; font-size: 16px; cursor: pointer;
  transition: var(--transition);
}
.play-btn:hover { background: var(--accent-hover); box-shadow: 0 4px 12px rgba(108,99,255,.4); }
.time-display { font-size: 12px; color: var(--text3); font-family: monospace; }
.voice-settings { padding: 16px; }
.setting-row {
  display: flex; align-items: center; justify-content: space-between;
  padding: 8px 0; border-bottom: 1px solid rgba(35,39,56,.5);
}
.setting-row:last-child { border-bottom: none; }
.setting-row .sr-label { font-size: 12px; color: var(--text2); }
.setting-row .sr-value { font-size: 12px; font-weight: 600; color: var(--text); }

/* ============ EXPORT CENTER ============ */
.export-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 20px; }
.export-card {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: var(--radius); padding: 20px;
  text-align: center; transition: var(--transition);
  cursor: pointer;
}
.export-card:hover { border-color: var(--accent); transform: translateY(-2px); box-shadow: var(--shadow-glow); }
.export-card.selected { border-color: var(--accent); background: rgba(108,99,255,.06); }
.export-card .ec-ratio {
  width: 48px; height: 48px; border: 2px solid var(--border-light);
  border-radius: 6px; margin: 0 auto 12px;
  display: flex; align-items: center; justify-content: center;
  transition: var(--transition);
}
.export-card:hover .ec-ratio, .export-card.selected .ec-ratio { border-color: var(--accent); }
.export-card .ec-ratio.ratio-916 { width: 32px; height: 56px; }
.export-card .ec-ratio.ratio-169 { width: 56px; height: 32px; }
.export-card .ec-ratio.ratio-11 { width: 44px; height: 44px; }
.export-card .ec-label { font-size: 14px; font-weight: 700; margin-bottom: 4px; }
.export-card .ec-desc { font-size: 11px; color: var(--text3); }
.export-card .ec-size { font-size: 11px; color: var(--text3); margin-top: 6px; font-family: monospace; }

.ab-variant-row {
  display: flex; align-items: center; gap: 16px;
  padding: 16px 20px; background: var(--bg2);
  border: 1px solid var(--border); border-radius: var(--radius);
}
.ab-variant-row .ab-label {
  width: 60px; height: 60px; border-radius: var(--radius-sm);
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; font-weight: 800; flex-shrink: 0;
}
.ab-variant-row .ab-info { flex: 1; }
.ab-variant-row .ab-info h4 { font-size: 13px; font-weight: 700; }
.ab-variant-row .ab-info p { font-size: 11px; color: var(--text2); margin-top: 2px; }

.export-summary {
  background: linear-gradient(135deg, rgba(108,99,255,.08), rgba(79,172,254,.05));
  border: 1px solid rgba(108,99,255,.2);
  border-radius: var(--radius); padding: 24px;
}
.export-summary h3 { font-size: 16px; font-weight: 700; margin-bottom: 16px; }
.export-items { display: flex; flex-direction: column; gap: 10px; }
.export-item {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 14px; background: rgba(0,0,0,.2);
  border-radius: var(--radius-sm);
}
.export-item .ei-icon { font-size: 18px; }
.export-item .ei-info { flex: 1; }
.export-item .ei-info .ei-name { font-size: 13px; font-weight: 600; }
.export-item .ei-info .ei-detail { font-size: 11px; color: var(--text3); }
.export-item .ei-status { font-size: 11px; }

/* ============ COMPLIANCE BAR ============ */
.compliance-bar {
  background: rgba(240,192,64,.08);
  border: 1px solid rgba(240,192,64,.2);
  border-radius: var(--radius); padding: 12px 16px;
  display: flex; align-items: center; gap: 10px;
  font-size: 12px; color: var(--gold); margin-bottom: 16px;
}
.compliance-bar .cb-icon { font-size: 16px; }

/* ============ MODAL ============ */
.modal-overlay {
  position: fixed; inset: 0; background: rgba(0,0,0,.6);
  backdrop-filter: blur(4px); z-index: 1000;
  display: none; align-items: center; justify-content: center;
}
.modal-overlay.show { display: flex; }
.modal {
  background: var(--bg2); border: 1px solid var(--border);
  border-radius: 16px; width: 520px; max-width: 90vw;
  max-height: 80vh; overflow-y: auto;
  box-shadow: 0 24px 80px rgba(0,0,0,.5);
  animation: modalIn .3s ease;
}
@keyframes modalIn { from { opacity: 0; transform: scale(.95) translateY(10px); } to { opacity: 1; transform: scale(1) translateY(0); } }
.modal-header {
  padding: 20px 24px; border-bottom: 1px solid var(--border);
  display: flex; align-items: center; justify-content: space-between;
}
.modal-header h3 { font-size: 16px; font-weight: 700; }
.modal-close {
  width: 32px; height: 32px; border-radius: 8px;
  background: var(--bg3); border: 1px solid var(--border);
  color: var(--text3); display: flex; align-items: center;
  justify-content: center; cursor: pointer; font-size: 16px;
  transition: var(--transition);
}
.modal-close:hover { color: #ff6b6b; border-color: #ff6b6b; }
.modal-body { padding: 24px; }
.modal-footer {
  padding: 16px 24px; border-top: 1px solid var(--border);
  display: flex; justify-content: flex-end; gap: 10px;
}

/* ============ RESPONSIVE ============ */
@media(max-width: 1200px) {
  .dashboard-stats { grid-template-columns: repeat(2, 1fr); }
  .project-row { grid-template-columns: 1fr 100px 80px 60px; }
  .project-row .proj-market, .project-row .proj-date { display: none; }
  .script-layout, .storyboard-layout, .voiceover-layout { grid-template-columns: 1fr; }
}
@media(max-width: 900px) {
  :root { --sidebar-w: 60px; }
  .sidebar-brand, .nav-section-label, .nav-item span:not(.nav-icon),
  .user-info, .nav-badge { display: none; }
  .sidebar-header { justify-content: center; padding: 12px 8px; }
  .nav-item { justify-content: center; padding: 10px; }
  .nav-item .nav-icon { width: 32px; height: 32px; }
  .sidebar-user { justify-content: center; }
  .dashboard-stats { grid-template-columns: 1fr; }
  .scene-grid { grid-template-columns: 1fr; }
  .export-grid { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<div class="app-layout">
  <!-- ==================== SIDEBAR ==================== -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-logo">A</div>
      <div class="sidebar-brand">
        AdCraft Studio
        <small>广告视频制作平台</small>
      </div>
    </div>

    <nav class="sidebar-nav">
      <div class="nav-section">
        <div class="nav-section-label">概览</div>
        <div class="nav-item active" onclick="switchPage('dashboard', this)">
          <span class="nav-icon">📊</span>
          <span>项目列表</span>
        </div>
      </div>

      <div class="nav-section">
        <div class="nav-section-label">当前项目 — PayEase Wallet</div>
        <div class="nav-item" onclick="switchPage('script', this)">
          <span class="nav-icon">📝</span>
          <span>剧本编辑</span>
          <span class="nav-badge">1/6</span>
        </div>
        <div class="nav-item" onclick="switchPage('style', this)">
          <span class="nav-icon">🎨</span>
          <span>全局设定</span>
          <span class="nav-badge warn">待确认</span>
        </div>
        <div class="nav-item" onclick="switchPage('scenes', this)">
          <span class="nav-icon">🎬</span>
          <span>场景资产</span>
          <span class="nav-badge">3</span>
        </div>
        <div class="nav-item" onclick="switchPage('storyboard', this)">
          <span class="nav-icon">🎞️</span>
          <span>分镜脚本</span>
        </div>
        <div class="nav-item" onclick="switchPage('voiceover', this)">
          <span class="nav-icon">🎙️</span>
          <span>配音工作台</span>
        </div>
        <div class="nav-item" onclick="switchPage('export', this)">
          <span class="nav-icon">📤</span>
          <span>导出中心</span>
        </div>
      </div>

      <div class="nav-section">
        <div class="nav-section-label">快捷操作</div>
        <div class="nav-item" onclick="openNewProjectModal()">
          <span class="nav-icon">➕</span>
          <span>新建项目</span>
        </div>
        <div class="nav-item">
          <span class="nav-icon">📋</span>
          <span>模板库</span>
        </div>
      </div>
    </nav>

    <div class="sidebar-footer">
      <div class="sidebar-user">
        <div class="user-avatar">K</div>
        <div class="user-info">
          <div class="name">Kevin</div>
          <div class="role">高级制作人</div>
        </div>
      </div>
    </div>
  </aside>

  <!-- ==================== MAIN AREA ==================== -->
  <div class="main-area">
    <!-- Top Bar -->
    <div class="topbar">
      <div class="topbar-breadcrumb">
        <span class="breadcrumb-item">项目列表</span>
        <span class="breadcrumb-sep">›</span>
        <span class="breadcrumb-item current" id="breadcrumb-current">PayEase Wallet</span>
      </div>
      <div class="topbar-actions">
        <button class="topbar-btn" title="通知">🔔</button>
        <button class="topbar-btn" title="帮助">❓</button>
        <button class="topbar-btn primary" title="保存" onclick="showToast('项目已保存')">💾</button>
      </div>
    </div>

    <!-- Content Area -->
    <div class="content-area">

      <!-- ========== PAGE: DASHBOARD ========== -->
      <div class="page active" id="page-dashboard">
        <div class="page-header" style="display:flex;align-items:center;justify-content:space-between;">
          <div>
            <h1>项目列表</h1>
            <p>管理所有广告视频项目，追踪制作进度</p>
          </div>
          <button class="btn btn-primary" onclick="openNewProjectModal()">+ 新建项目</button>
        </div>

        <div class="dashboard-stats">
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(108,99,255,.12);">📁</div>
            <div class="stat-value" style="color:var(--accent);">12</div>
            <div class="stat-label">总项目数</div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(67,233,123,.12);">✅</div>
            <div class="stat-value" style="color:#43e97b;">5</div>
            <div class="stat-label">已完成</div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(247,151,30,.12);">⏳</div>
            <div class="stat-value" style="color:#f7971e;">4</div>
            <div class="stat-label">进行中</div>
          </div>
          <div class="stat-card">
            <div class="stat-icon" style="background:rgba(79,172,254,.12);">🌍</div>
            <div class="stat-value" style="color:#4facfe;">3</div>
            <div class="stat-label">目标市场</div>
          </div>
        </div>

        <div class="project-list">
          <div class="project-row" onclick="switchPage('script', document.querySelectorAll('.nav-item')[2])">
            <div class="proj-info">
              <div class="proj-icon" style="background:rgba(108,99,255,.15);">💳</div>
              <div>
                <div class="proj-name">PayEase Wallet</div>
                <div class="proj-desc">数字钱包 · 东南亚市场推广</div>
              </div>
            </div>
            <div class="proj-market"><span class="tag tag-blue">🇸🇬 东南亚</span></div>
            <div class="proj-stage">
              <div class="progress-bar"><div class="fill" style="width:35%;background:linear-gradient(90deg,#6c63ff,#4facfe);"></div></div>
              <div style="font-size:10px;color:var(--text3);margin-top:4px;">剧本编辑中</div>
            </div>
            <div class="proj-date">2026-05-04</div>
            <div>
              <span class="tag tag-purple">30s 竖版</span>
            </div>
          </div>

          <div class="project-row">
            <div class="proj-info">
              <div class="proj-icon" style="background:rgba(67,233,123,.15);">📈</div>
              <div>
                <div class="proj-name">WealthGrow Pro</div>
                <div class="proj-desc">智能理财平台 · 北美市场</div>
              </div>
            </div>
            <div class="proj-market"><span class="tag tag-green">🇺🇸 北美</span></div>
            <div class="proj-stage">
              <div class="progress-bar"><div class="fill" style="width:100%;background:linear-gradient(90deg,#43e97b,#06d6a0);"></div></div>
              <div style="font-size:10px;color:#43e97b;margin-top:4px;">已导出</div>
            </div>
            <div class="proj-date">2026-05-02</div>
            <div>
              <span class="tag tag-orange">60s 横版</span>
            </div>
          </div>

          <div class="project-row">
            <div class="proj-info">
              <div class="proj-icon" style="background:rgba(240,192,64,.15);">🪙</div>
              <div>
                <div class="proj-name">CryptoVault</div>
                <div class="proj-desc">加密资产托管 · 中东市场</div>
              </div>
            </div>
            <div class="proj-market"><span class="tag tag-gold">🇦🇪 中东</span></div>
            <div class="proj-stage">
              <div class="progress-bar"><div class="fill" style="width:60%;background:linear-gradient(90deg,#f7971e,#ff6b6b);"></div></div>
              <div style="font-size:10px;color:var(--text3);margin-top:4px;">分镜中</div>
            </div>
            <div class="proj-date">2026-05-01</div>
            <div>
              <span class="tag tag-purple">15s 竖版</span>
            </div>
          </div>

          <div class="project-row">
            <div class="proj-info">
              <div class="proj-icon" style="background:rgba(79,172,254,.15);">🏦</div>
              <div>
                <div class="proj-name">SwiftPay International</div>
                <div class="proj-desc">跨境支付 · 全球多市场</div>
              </div>
            </div>
            <div class="proj-market"><span class="tag tag-blue">🌍 全球</span></div>
            <div class="proj-stage">
              <div class="progress-bar"><div class="fill" style="width:15%;background:linear-gradient(90deg,#4facfe,#6c63ff);"></div></div>
              <div style="font-size:10px;color:var(--text3);margin-top:4px;">剧本中</div>
            </div>
            <div class="proj-date">2026-05-03</div>
            <div>
              <span class="tag tag-red">A/B测试</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ========== PAGE: SCRIPT EDITOR ========== -->
      <div class="page" id="page-script">
        <div class="page-header">
          <h1>剧本编辑 — PayEase Wallet</h1>
          <p>结构化剧本编辑，支持 AIDA / PAS 广告框架</p>
        </div>

        <!-- Compliance Notice -->
        <div class="compliance-bar">
          <span class="cb-icon">⚠️</span>
          <span><strong>合规提醒：</strong>目标市场为东南亚，请确保广告文案符合当地金融广告法规（MAS / OJK / SEC），必要时添加风险提示语。</span>
          <button class="btn btn-sm btn-ghost" style="margin-left:auto;color:var(--gold);">查看法规</button>
        </div>

        <!-- Project Info -->
        <div class="card" style="margin-bottom:20px;">
          <div class="grid-4">
            <div class="input-group">
              <label>产品名称</label>
              <input class="input-field" value="PayEase Wallet — 数字钱包">
            </div>
            <div class="input-group">
              <label>目标市场</label>
              <select class="input-field">
                <option>🇸🇬 新加坡 / 东南亚</option>
                <option>🇺🇸 北美</option>
                <option>🇦🇪 中东</option>
                <option>🇯🇵 日本</option>
                <option>🌍 全球</option>
              </select>
            </div>
            <div class="input-group">
              <label>视频时长</label>
              <select class="input-field">
                <option selected>30 秒</option>
                <option>15 秒</option>
                <option>60 秒</option>
              </select>
            </div>
            <div class="input-group">
              <label>广告模板</label>
              <select class="input-field">
                <option selected>AIDA（注意力-兴趣-欲望-行动）</option>
                <option>PAS（痛点-放大-解决）</option>
                <option>自定义</option>
              </select>
            </div>
          </div>
        </div>

        <div class="script-layout">
          <div class="script-main">
            <div class="card">
              <div class="card-header">
                <h3>📝 剧本内容（AIDA 框架）</h3>
                <div class="card-action">✨ AI 优化剧本</div>
              </div>
              <div style="display:flex;flex-direction:column;gap:12px;">
                <div class="script-block attention">
                  <span class="block-label"><span class="badge" style="background:rgba(255,107,107,.2);color:#ff6b6b;">A</span> Attention — 注意力</span>
                  <span class="block-time">0-5s</span>
                  <div class="block-content" contenteditable="true">还在为跨境转账的手续费头疼吗？每次汇款都被银行扣掉一笔？</div>
                </div>
                <div class="script-block interest">
                  <span class="block-label"><span class="badge" style="background:rgba(247,151,30,.2);color:#f7971e;">I</span> Interest — 兴趣</span>
                  <span class="block-time">5-15s</span>
                  <div class="block-content" contenteditable="true">PayEase 让你用手机就能完成全球转账，0 手续费，3 秒到账。支持 50+ 种货币，覆盖 180+ 个国家。</div>
                </div>
                <div class="script-block desire">
                  <span class="block-label"><span class="badge" style="background:rgba(67,233,123,.2);color:#43e97b;">D</span> Desire — 欲望</span>
                  <span class="block-time">15-25s</span>
                  <div class="block-content" contenteditable="true">已有超过 500 万用户信赖 PayEase 管理他们的跨境资金。银行级安全加密，你的每一分钱都受到保护。</div>
                </div>
                <div class="script-block action">
                  <span class="block-label"><span class="badge" style="background:rgba(79,172,254,.2);color:#4facfe;">A</span> Action — 行动</span>
                  <span class="block-time">25-30s</span>
                  <div class="block-content" contenteditable="true">立即下载 PayEase，新用户注册送 $5 优惠券。*使用金融服务存在风险，请仔细阅读条款</div>
                </div>
              </div>
            </div>

            <!-- Target Audience -->
            <div class="card">
              <div class="card-header"><h3>🎯 目标受众</h3></div>
              <div class="grid-3">
                <div>
                  <div style="font-size:11px;color:var(--text3);margin-bottom:6px;">年龄段</div>
                  <div style="display:flex;flex-wrap:wrap;gap:6px;">
                    <span class="tag tag-purple">18-25</span>
                    <span class="tag tag-purple active" style="background:rgba(108,99,255,.3);">25-35</span>
                    <span class="tag tag-purple active" style="background:rgba(108,99,255,.3);">35-45</span>
                    <span class="tag tag-purple">45+</span>
                  </div>
                </div>
                <div>
                  <div style="font-size:11px;color:var(--text3);margin-bottom:6px;">用户痛点</div>
                  <div style="display:flex;flex-wrap:wrap;gap:6px;">
                    <span class="tag tag-red">手续费高</span>
                    <span class="tag tag-red">到账慢</span>
                    <span class="tag tag-red">流程复杂</span>
                    <span class="tag tag-orange">汇率不透明</span>
                  </div>
                </div>
                <div>
                  <div style="font-size:11px;color:var(--text3);margin-bottom:6px;">使用场景</div>
                  <div style="display:flex;flex-wrap:wrap;gap:6px;">
                    <span class="tag tag-blue">海外留学</span>
                    <span class="tag tag-blue">跨境贸易</span>
                    <span class="tag tag-blue">旅行消费</span>
                    <span class="tag tag-green">远程工作收款</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Panel -->
          <div class="script-sidebar-panel">
            <!-- Selling Points -->
            <div class="card">
              <div class="card-header">
                <h3>💡 核心卖点</h3>
                <div class="card-action">+ 添加</div>
              </div>
              <div style="display:flex;flex-direction:column;gap:8px;">
                <div class="selling-point">
                  <span class="sp-num">1</span>
                  <div>
                    <div style="font-size:12px;font-weight:600;">0 手续费</div>
                    <div style="font-size:10px;color:var(--text3);">跨境转账零手续费</div>
                  </div>
                </div>
                <div class="selling-point">
                  <span class="sp-num">2</span>
                  <div>
                    <div style="font-size:12px;font-weight:600;">3 秒到账</div>
                    <div style="font-size:10px;color:var(--text3);">实时到账，全球网络</div>
                  </div>
                </div>
                <div class="selling-point">
                  <span class="sp-num">3</span>
                  <div>
                    <div style="font-size:12px;font-weight:600;">银行级安全</div>
                    <div style="font-size:10px;color:var(--text3);">256位加密 + 双因素认证</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Upload Zone -->
            <div class="card">
              <div class="card-header">
                <h3>📎 产品素材</h3>
              </div>
              <div class="upload-zone" onclick="simulateUpload()">
                <div class="upload-icon">📤</div>
                <div class="upload-text">点击或拖拽上传素材</div>
                <div class="upload-hint">支持 PNG / JPG / MP4，单文件 ≤ 50MB</div>
              </div>
              <div class="uploaded-files" id="uploaded-files">
                <div class="uploaded-file">
                  <span class="file-icon">📱</span>
                  <span class="file-name">payease_home_v2.png</span>
                  <span class="file-size">2.4 MB</span>
                  <span class="file-remove" onclick="this.parentElement.remove()">✕</span>
                </div>
                <div class="uploaded-file">
                  <span class="file-icon">📱</span>
                  <span class="file-name">payease_transfer.png</span>
                  <span class="file-size">1.8 MB</span>
                  <span class="file-remove" onclick="this.parentElement.remove()">✕</span>
                </div>
                <div class="uploaded-file">
                  <span class="file-icon">🖼️</span>
                  <span class="file-name">brand_logo.svg</span>
                  <span class="file-size">24 KB</span>
                  <span class="file-remove" onclick="this.parentElement.remove()">✕</span>
                </div>
              </div>
            </div>

            <!-- Risk Notice -->
            <div class="card" style="border-color:rgba(240,192,64,.25);">
              <div class="card-header"><h3 style="color:var(--gold);">⚖️ 合规文案</h3></div>
              <div style="font-size:12px;color:var(--text2);line-height:1.7;">
                <div style="margin-bottom:8px;"><strong style="color:var(--text);">风险提示语（已自动添加至 Action 段落）：</strong></div>
                <div style="background:var(--bg3);padding:10px;border-radius:6px;font-size:11px;color:var(--text3);">
                  "Investment and financial services involve risk. Past performance does not guarantee future results. Please read the terms and conditions carefully before using this service."
                </div>
                <div style="margin-top:10px;display:flex;gap:6px;">
                  <span class="tag tag-gold">MAS 合规</span>
                  <span class="tag tag-gold">风险提示</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ========== PAGE: GLOBAL STYLE ========== -->
      <div class="page" id="page-style">
        <div class="page-header">
          <h1>全局风格设定</h1>
          <p>确定广告的视觉与音频基调，建立统一的风格指南</p>
        </div>

        <div class="grid-2">
          <!-- Visual Settings -->
          <div class="card">
            <div class="card-header"><h3>🎨 视觉规范</h3></div>
            <div style="display:flex;flex-direction:column;gap:16px;">
              <div class="input-group">
                <label>画幅比例</label>
                <div style="display:flex;gap:8px;">
                  <div class="export-card selected" style="padding:12px;flex:1;cursor:pointer;" onclick="this.parentElement.querySelectorAll('.export-card').forEach(c=>c.classList.remove('selected'));this.classList.add('selected');">
                    <div class="ec-ratio ratio-916"></div>
                    <div class="ec-label">9:16 竖版</div>
                    <div class="ec-desc">抖音 / TikTok / Reels</div>
                  </div>
                  <div class="export-card" style="padding:12px;flex:1;cursor:pointer;" onclick="this.parentElement.querySelectorAll('.export-card').forEach(c=>c.classList.remove('selected'));this.classList.add('selected');">
                    <div class="ec-ratio ratio-169"></div>
                    <div class="ec-label">16:9 横版</div>
                    <div class="ec-desc">YouTube / B站</div>
                  </div>
                  <div class="export-card" style="padding:12px;flex:1;cursor:pointer;" onclick="this.parentElement.querySelectorAll('.export-card').forEach(c=>c.classList.remove('selected'));this.classList.add('selected');">
                    <div class="ec-ratio ratio-11"></div>
                    <div class="ec-label">1:1 方形</div>
                    <div class="ec-desc">Instagram / 朋友圈</div>
                  </div>
                </div>
              </div>
              <div class="input-group">
                <label>品牌主色</label>
                <div style="display:flex;gap:8px;align-items:center;">
                  <div style="width:40px;height:40px;border-radius:8px;background:#1a73e8;border:2px solid var(--border);cursor:pointer;"></div>
                  <input class="input-field" value="#1A73E8" style="width:120px;font-family:monospace;">
                  <div style="display:flex;gap:4px;">
                    <div style="width:28px;height:28px;border-radius:6px;background:#6c63ff;cursor:pointer;" title="#6C63FF"></div>
                    <div style="width:28px;height:28px;border-radius:6px;background:#43e97b;cursor:pointer;" title="#43E97B"></div>
                    <div style="width:28px;height:28px;border-radius:6px;background:#f7971e;cursor:pointer;" title="#F7971E"></div>
                    <div style="width:28px;height:28px;border-radius:6px;background:#e040fb;cursor:pointer;" title="#E040FB"></div>
                    <div style="width:28px;height:28px;border-radius:6px;background:#0ea5e9;cursor:pointer;" title="#0EA5E9"></div>
                  </div>
                </div>
              </div>
              <div class="input-group">
                <label>视觉风格</label>
                <div style="display:flex;flex-wrap:wrap;gap:8px;">
                  <span class="tag tag-purple" style="cursor:pointer;padding:8px 14px;">🏢 商务专业</span>
                  <span class="tag tag-purple" style="cursor:pointer;padding:8px 14px;">✨ 科技未来</span>
                  <span class="tag tag-purple active" style="cursor:pointer;padding:8px 14px;background:rgba(108,99,255,.3);">👤 生活场景</span>
                  <span class="tag tag-purple" style="cursor:pointer;padding:8px 14px;">📊 数据可视化</span>
                  <span class="tag tag-purple" style="cursor:pointer;padding:8px 14px;">🌍 国际化</span>
                </div>
              </div>
              <div class="input-group">
                <label>镜头语言</label>
                <select class="input-field">
                  <option>稳定器跟拍 — 跟随人物自然移动</option>
                  <option>快节奏剪辑 — 短镜头切换，适合短视频</option>
                  <option>慢镜 + 升格 — 强调情感和质感</option>
                  <option>产品特写 + 环境全景 — 兼顾展示与氛围</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Audio & Typography -->
          <div class="card">
            <div class="card-header"><h3>🔊 音频与排版</h3></div>
            <div style="display:flex;flex-direction:column;gap:16px;">
              <div class="input-group">
                <label>BGM 风格</label>
                <div style="display:flex;gap:8px;flex-wrap:wrap;">
                  <span class="tag tag-blue" style="cursor:pointer;padding:8px 14px;">🎵 轻快电子</span>
                  <span class="tag tag-blue active" style="cursor:pointer;padding:8px 14px;background:rgba(79,172,254,.3);">🎹 现代钢琴</span>
                  <span class="tag tag-blue" style="cursor:pointer;padding:8px 14px;">🎸 流行</span>
                  <span class="tag tag-blue" style="cursor:pointer;padding:8px 14px;">🎻 古典</span>
                  <span class="tag tag-blue" style="cursor:pointer;padding:8px 14px;">🔇 无背景乐</span>
                </div>
              </div>
              <div class="input-group">
                <label>旁白风格</label>
                <div class="grid-2">
                  <select class="input-field">
                    <option>女声 — 温暖、信任感</option>
                    <option>男声 — 专业、沉稳</option>
                    <option>青年 — 活力、亲切</option>
                  </select>
                  <select class="input-field">
                    <option>语速：正常 (4字/秒)</option>
                    <option>语速：稍快 (5字/秒)</option>
                    <option>语速：较慢 (3字/秒)</option>
                  </select>
                </div>
              </div>
              <div class="input-group">
                <label>字体选择</label>
                <div style="display:flex;gap:8px;flex-wrap:wrap;">
                  <span class="tag tag-green active" style="cursor:pointer;padding:8px 14px;background:rgba(67,233,123,.25);">PingFang SC</span>
                  <span class="tag tag-green" style="cursor:pointer;padding:8px 14px;">SF Pro Display</span>
                  <span class="tag tag-green" style="cursor:pointer;padding:8px 14px;">Inter</span>
                  <span class="tag tag-green" style="cursor:pointer;padding:8px 14px;">DIN Pro</span>
                </div>
              </div>
              <div class="input-group">
                <label>字幕样式</label>
                <div style="display:flex;gap:8px;">
                  <div style="flex:1;padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;text-align:center;cursor:pointer;">
                    <div style="font-size:18px;font-weight:700;margin-bottom:4px;">底部居中</div>
                    <div style="font-size:10px;color:var(--text3);">经典位置</div>
                  </div>
                  <div style="flex:1;padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;text-align:center;cursor:pointer;">
                    <div style="font-size:18px;font-weight:700;margin-bottom:4px;">底部居中</div>
                    <div style="font-size:10px;color:var(--text3);">经典位置</div>
                  </div>
                  <div style="flex:1;padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:8px;text-align:center;cursor:pointer;">
                    <div style="font-size:18px;font-weight:700;margin-bottom:4px;">底部居中</div>
                    <div style="font-size:10px;color:var(--text3);">经典位置</div>
                  </div>
                </div>
              </div>
              <div style="display:flex;gap:10px;margin-top:8px;">
                <button class="btn btn-primary" style="flex:1;">确认风格设定</button>
                <button class="btn btn-secondary">预览效果</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ========== PAGE: SCENE ASSETS ========== -->
      <div class="page" id="page-scenes">
        <div class="page-header" style="display:flex;align-items:center;justify-content:space-between;">
          <div>
            <h1>场景资产管理</h1>
            <p>管理场景视觉元素、角色设定、产品素材和 AI 生图 Prompt</p>
          </div>
          <div style="display:flex;gap:8px;">
            <button class="btn btn-secondary">📥 批量导入 Prompt</button>
            <button class="btn btn-primary">+ 添加场景</button>
          </div>
        </div>

        <!-- Uploaded Screenshots Preview -->
        <div class="card" style="margin-bottom:20px;">
          <div class="card-header">
            <h3>📱 已上传的产品截图（手机 Mockup 预览）</h3>
            <div class="card-action">+ 上传更多截图</div>
          </div>
          <div style="display:flex;gap:24px;align-items:center;padding:16px 0;">
            <div style="text-align:center;">
              <div class="phone-mockup">
                <div class="phone-notch"></div>
                <div class="phone-screen">
                  <div class="app-icon">💳</div>
                  <div class="app-name">PayEase</div>
                  <div style="width:100%;height:1px;background:#333;margin:4px 0;"></div>
                  <div class="app-balance">$12,450.00</div>
                  <div style="font-size:5px;color:#888;">总资产</div>
                  <div style="display:flex;gap:8px;margin-top:6px;">
                    <div style="width:24px;height:24px;background:#1a73e8;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:8px;">↑</div>
                    <div style="width:24px;height:24px;background:#333;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:8px;">↓</div>
                    <div style="width:24px;height:24px;background:#333;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:8px;">⟳</div>
                  </div>
                </div>
              </div>
              <div style="font-size:10px;color:var(--text3);margin-top:8px;">首页 · 总资产</div>
            </div>
            <div style="text-align:center;">
              <div class="phone-mockup">
                <div class="phone-notch"></div>
                <div class="phone-screen">
                  <div style="font-size:6px;color:#888;width:100%;text-align:left;">← 转账</div>
                  <div style="font-size:7px;color:#fff;font-weight:600;margin:4px 0;">发送至</div>
                  <div style="width:100%;background:#222;border-radius:4px;padding:6px;font-size:6px;color:#888;">收款人姓名或手机号</div>
                  <div style="font-size:7px;color:#fff;margin-top:6px;">金额</div>
                  <div style="font-size:14px;color:#43e97b;font-weight:700;">$500.00</div>
                  <div style="font-size:5px;color:#888;">≈ ¥3,620.00 CNY</div>
                  <div style="width:100%;background:#1a73e8;border-radius:4px;padding:4px;text-align:center;margin-top:8px;font-size:6px;color:#fff;">确认转账</div>
                </div>
              </div>
              <div style="font-size:10px;color:var(--text3);margin-top:8px;">转账页面</div>
            </div>
            <div style="text-align:center;">
              <div class="phone-mockup">
                <div class="phone-notch"></div>
                <div class="phone-screen">
                  <div style="font-size:6px;color:#888;width:100%;text-align:left;">← 交易记录</div>
                  <div style="display:flex;flex-direction:column;gap:4px;width:100%;margin-top:6px;">
                    <div style="display:flex;justify-content:space-between;font-size:5px;padding:4px;background:#222;border-radius:3px;">
                      <span style="color:#fff;">→ 李明</span><span style="color:#ff6b6b;">-$200.00</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;font-size:5px;padding:4px;background:#222;border-radius:3px;">
                      <span style="color:#fff;">← 工资入账</span><span style="color:#43e97b;">+$5,000</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;font-size:5px;padding:4px;background:#222;border-radius:3px;">
                      <span style="color:#fff;">→ Netflix</span><span style="color:#ff6b6b;">-$15.99</span>
                    </div>
                    <div style="display:flex;justify-content:space-between;font-size:5px;padding:4px;background:#222;border-radius:3px;">
                      <span style="color:#fff;">← 退款</span><span style="color:#43e97b;">+$89.00</span>
                    </div>
                  </div>
                </div>
              </div>
              <div style="font-size:10px;color:var(--text3);margin-top:8px;">交易记录</div>
            </div>
            <div style="flex:1;">
              <div style="background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);padding:14px;">
                <div style="font-size:12px;font-weight:600;color:var(--text);margin-bottom:8px;">截图使用建议</div>
                <div style="font-size:11px;color:var(--text2);line-height:1.8;">
                  <div>✅ <strong>场景1（Attention）</strong>：首页截图嵌入手机 Mockup，展示总资产界面</div>
                  <div>✅ <strong>场景2（Interest）</strong>：转账页面全屏 + 指针动画演示 3 秒到账</div>
                  <div>✅ <strong>场景4（Desire）</strong>：交易记录展示资金流动，配合数据可视化</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Scene Cards Grid -->
        <div class="scene-grid">
          <div class="scene-card">
            <div class="scene-preview" style="background:linear-gradient(135deg,#1a1a3e,#0d1b2a);">
              <div style="font-size:48px;opacity:.25;">🏢</div>
              <div class="scene-overlay"><span class="scene-status done">✓ 已生成</span></div>
            </div>
            <div class="scene-card-body">
              <h4>场景 1：痛点引入</h4>
              <div class="scene-desc">年轻人在银行柜台前无奈等待，窗外阳光明媚，形成反差</div>
              <div style="display:flex;gap:4px;margin-bottom:6px;">
                <span class="tag tag-purple" style="font-size:9px;">实景 + 真人</span>
                <span class="tag tag-blue" style="font-size:9px;">0-5s</span>
              </div>
              <div class="scene-prompt">A frustrated young professional standing at a bank counter, looking at high transfer fees on a receipt, warm cinematic lighting, shallow depth of field, 4K, professional photography</div>
            </div>
          </div>

          <div class="scene-card">
            <div class="scene-preview" style="background:linear-gradient(135deg,#0d2b1a,#1a1a3e);">
              <div style="display:flex;align-items:center;gap:8px;">
                <div class="phone-mockup" style="transform:scale(.7);margin:-20px;">
                  <div class="phone-notch"></div>
                  <div class="phone-screen"><div class="app-icon">💳</div><div class="app-name">PayEase</div><div class="app-balance">$12,450</div></div>
                </div>
                <div style="font-size:24px;opacity:.3;">✨</div>
              </div>
              <div class="scene-overlay"><span class="scene-status done">✓ 已生成</span></div>
            </div>
            <div class="scene-card-body">
              <h4>场景 2：产品展示</h4>
              <div class="scene-desc">手机 Mockup 中展示 PayEase 首页，配合光效和动效强调"0 手续费"</div>
              <div style="display:flex;gap:4px;margin-bottom:6px;">
                <span class="tag tag-green" style="font-size:9px;">产品截图</span>
                <span class="tag tag-blue" style="font-size:9px;">5-15s</span>
                <span class="tag tag-gold" style="font-size:9px;">Mockup</span>
              </div>
              <div class="scene-prompt">Premium smartphone mockup floating in air, displaying fintech app dashboard with clean UI, blue accent glow, dark elegant background, bokeh lights, cinematic quality, 8K, sharp focus</div>
            </div>
          </div>

          <div class="scene-card">
            <div class="scene-preview" style="background:linear-gradient(135deg,#2b1a0d,#1a1a3e);">
              <div style="font-size:48px;opacity:.25;">🌍</div>
              <div class="scene-overlay"><span class="scene-status pending">⟳ 生成中 68%</span></div>
            </div>
            <div class="scene-card-body">
              <h4>场景 3：信任背书</h4>
              <div class="scene-desc">全球地图动画展示覆盖 180+ 国家，配合数据数字滚动效果</div>
              <div style="display:flex;gap:4px;margin-bottom:6px;">
                <span class="tag tag-orange" style="font-size:9px;">数据可视化</span>
                <span class="tag tag-blue" style="font-size:9px;">15-25s</span>
              </div>
              <div class="scene-prompt">Holographic world map with glowing connection lines between cities, data visualization overlay, futuristic fintech aesthetic, dark background with blue and gold accents, 3D render, 4K</div>
            </div>
          </div>

          <div class="scene-card">
            <div class="scene-preview" style="background:var(--bg3);border:2px dashed var(--border-light);">
              <div style="text-align:center;">
                <div style="font-size:32px;opacity:.3;">➕</div>
                <div style="font-size:11px;color:var(--text3);margin-top:6px;">添加新场景</div>
              </div>
              <div class="scene-overlay"><span class="scene-status empty">待创建</span></div>
            </div>
            <div class="scene-card-body">
              <h4 style="color:var(--text3);">场景 4：行动召唤</h4>
              <div class="scene-desc" style="color:var(--text3);">品牌 Logo + 下载引导 + CTA 按钮</div>
            </div>
          </div>
        </div>
      </div>

      <!-- ========== PAGE: STORYBOARD ========== -->
      <div class="page" id="page-storyboard">
        <div class="page-header">
          <h1>分镜脚本</h1>
          <p>精确到秒的分镜编辑器，每个镜头含完整生成参数</p>
        </div>

        <div class="storyboard-layout">
          <div class="timeline-area">
            <!-- Video Layer -->
            <div class="timeline-track">
              <div class="track-header">
                <span class="track-label">🎬 视频轨</span>
                <span class="track-time">总时长 30s</span>
              </div>
              <div class="clips-row">
                <div class="clip clip-01 selected" onclick="selectClip(this, 1)" style="flex:2;">01</div>
                <div class="clip clip-02" onclick="selectClip(this, 2)" style="flex:5;">02</div>
                <div class="clip clip-03" onclick="selectClip(this, 3)" style="flex:5;">03</div>
                <div class="clip clip-04" onclick="selectClip(this, 4)" style="flex:3;">04</div>
              </div>
              <div class="timeline-ruler">
                <span class="ruler-mark">0s</span>
                <span class="ruler-mark">5s</span>
                <span class="ruler-mark">10s</span>
                <span class="ruler-mark">15s</span>
                <span class="ruler-mark">20s</span>
                <span class="ruler-mark">25s</span>
                <span class="ruler-mark">30s</span>
              </div>
            </div>

            <!-- Audio Layer -->
            <div class="timeline-track">
              <div class="track-header">
                <span class="track-label">🎙️ 旁白轨</span>
                <span class="track-time">30s 配音</span>
              </div>
              <div style="display:flex;gap:4px;height:32px;">
                <div style="flex:2;background:rgba(108,99,255,.2);border-radius:4px;border:1px solid rgba(108,99,255,.3);"></div>
                <div style="flex:5;background:rgba(255,107,107,.2);border-radius:4px;border:1px solid rgba(255,107,107,.3);"></div>
                <div style="flex:5;background:rgba(67,233,123,.2);border-radius:4px;border:1px solid rgba(67,233,123,.3);"></div>
                <div style="flex:3;background:rgba(79,172,254,.2);border-radius:4px;border:1px solid rgba(79,172,254,.3);"></div>
              </div>
            </div>

            <!-- BGM Layer -->
            <div class="timeline-track">
              <div class="track-header">
                <span class="track-label">🎵 BGM</span>
                <span class="track-time">30s 背景音乐</span>
              </div>
              <div style="height:24px;background:rgba(79,172,254,.08);border-radius:4px;border:1px solid rgba(79,172,254,.15);display:flex;align-items:center;justify-content:center;font-size:10px;color:var(--text3);">现代钢琴 · 轻快节奏 · 全程</div>
            </div>

            <!-- Subtitle Layer -->
            <div class="timeline-track">
              <div class="track-header">
                <span class="track-label">💬 字幕轨</span>
                <span class="track-time">4 条字幕</span>
              </div>
              <div style="display:flex;gap:4px;height:28px;align-items:center;">
                <div style="flex:2;background:rgba(240,192,64,.1);border-radius:4px;border:1px dashed rgba(240,192,64,.3);display:flex;align-items:center;justify-content:center;font-size:7px;color:var(--gold);">手续费高？</div>
                <div style="flex:5;background:rgba(240,192,64,.1);border-radius:4px;border:1px dashed rgba(240,192,64,.3);display:flex;align-items:center;justify-content:center;font-size:7px;color:var(--gold);">0手续费 3秒到账</div>
                <div style="flex:5;background:rgba(240,192,64,.1);border-radius:4px;border:1px dashed rgba(240,192,64,.3);display:flex;align-items:center;justify-content:center;font-size:7px;color:var(--gold);">500万用户信赖</div>
                <div style="flex:3;background:rgba(240,192,64,.1);border-radius:4px;border:1px dashed rgba(240,192,64,.3);display:flex;align-items:center;justify-content:center;font-size:7px;color:var(--gold);">立即下载</div>
              </div>
            </div>
          </div>

          <!-- Clip Detail Panel -->
          <div class="clip-detail-panel">
            <div class="clip-detail-header">
              <h3>镜头 01 详情</h3>
              <div style="display:flex;gap:6px;">
                <button class="btn btn-sm btn-secondary">AI 生成</button>
                <button class="btn btn-sm btn-ghost">编辑</button>
              </div>
            </div>
            <div class="clip-detail-body">
              <div class="clip-preview-area" id="clip-preview">🎬</div>
              <div class="detail-field">
                <div class="df-label">时间区间</div>
                <div class="df-value">0 - 5 秒（共 5s）</div>
              </div>
              <div class="detail-field">
                <div class="df-label">画面描述</div>
                <div class="df-value">银行柜台前，年轻人看着转账回执上高额手续费露出无奈表情，镜头从回执特写缓慢上移到人物表情</div>
              </div>
              <div class="detail-field">
                <div class="df-label">运镜</div>
                <div class="df-value">慢速推进 + 浅景深</div>
              </div>
              <div class="detail-field">
                <div class="df-label">旁白文案</div>
                <div class="df-value">"还在为跨境转账的手续费头疼吗？"</div>
              </div>
              <div class="detail-field">
                <div class="df-label">字幕</div>
                <div class="df-value" style="color:var(--gold);">跨境转账手续费太高？</div>
              </div>
              <div class="detail-field">
                <div class="df-label">转场</div>
                <div class="df-value">硬切 → 镜头 02</div>
              </div>
              <div class="detail-field">
                <div class="df-label">生成平台建议</div>
                <div class="df-value">可灵（Kling）/ Runway Gen-3 — 需要真人表情</div>
              </div>
              <div class="detail-field">
                <div class="df-label">参考素材</div>
                <div class="df-value">无（AI 生成场景）</div>
              </div>
              <div class="detail-field">
                <div class="df-label">AI Prompt（英文）</div>
                <div class="df-value" style="font-family:monospace;font-size:10px;color:var(--text3);background:var(--bg3);padding:8px;border-radius:6px;line-height:1.6;">
                  A frustrated young professional at a bank counter, looking at transfer receipt with high fees, warm cinematic lighting, shallow depth of field, slow push-in camera, 4K, professional cinematography
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ========== PAGE: VOICEOVER ========== -->
      <div class="page" id="page-voiceover">
        <div class="page-header">
          <h1>配音工作台</h1>
          <p>多平台 TTS 集成、声画同步预览、语速情绪精细控制</p>
        </div>

        <div class="voiceover-layout">
          <div class="voice-script">
            <div class="card">
              <div class="card-header">
                <h3>📝 配音脚本（逐镜头）</h3>
                <div style="display:flex;gap:8px;">
                  <button class="btn btn-sm btn-secondary">📥 导入剧本</button>
                  <button class="btn btn-sm btn-primary">✨ AI 分配配音</button>
                </div>
              </div>
              <div style="display:flex;flex-direction:column;gap:8px;">
                <div class="voice-line active">
                  <span class="vl-num">01</span>
                  <span class="vl-text">还在为跨境转账的手续费头疼吗？</span>
                  <span class="vl-voice"><select><option>女声-温暖</option><option>男声-专业</option></select></span>
                  <span class="vl-speed">4.0字/s</span>
                  <button class="vl-play">▶</button>
                </div>
                <div class="voice-line">
                  <span class="vl-num">02</span>
                  <span class="vl-text">PayEase 让你用手机就能完成全球转账</span>
                  <span class="vl-voice"><select><option>女声-温暖</option><option>男声-专业</option></select></span>
                  <span class="vl-speed">4.5字/s</span>
                  <button class="vl-play">▶</button>
                </div>
                <div class="voice-line">
                  <span class="vl-num">03</span>
                  <span class="vl-text">0 手续费，3 秒到账</span>
                  <span class="vl-voice"><select><option>女声-温暖</option><option>男声-专业</option></select></span>
                  <span class="vl-speed">3.5字/s</span>
                  <button class="vl-play">▶</button>
                </div>
                <div class="voice-line">
                  <span class="vl-num">04</span>
                  <span class="vl-text">支持 50+ 种货币，覆盖 180+ 个国家</span>
                  <span class="vl-voice"><select><option>女声-温暖</option><option>男声-专业</option></select></span>
                  <span class="vl-speed">4.0字/s</span>
                  <button class="vl-play">▶</button>
                </div>
                <div class="voice-line">
                  <span class="vl-num">05</span>
                  <span class="vl-text">超过 500 万用户的信赖之选</span>
                  <span class="vl-voice"><select><option>女声-温暖</option><option>男声-专业</option></select></span>
                  <span class="vl-speed">4.0字/s</span>
                  <button class="vl-play">▶</button>
                </div>
                <div class="voice-line">
                  <span class="vl-num">06</span>
                  <span class="vl-text">银行级安全加密，守护每一笔资金</span>
                  <span class="vl-voice"><select><option>女声-温暖</option><option>男声-专业</option></select></span>
                  <span class="vl-speed">4.0字/s</span>
                  <button class="vl-play">▶</button>
                </div>
                <div class="voice-line">
                  <span class="vl-num">07</span>
                  <span class="vl-text">立即下载 PayEase，新用户注册送 5 美元优惠券</span>
                  <span class="vl-voice"><select><option>女声-温暖</option><option>男声-专业</option></select></span>
                  <span class="vl-speed">4.5字/s</span>
                  <button class="vl-play">▶</button>
                </div>
              </div>
            </div>

            <!-- TTS Platform -->
            <div class="card">
              <div class="card-header"><h3>🌐 TTS 平台配置</h3></div>
              <div class="grid-2" style="gap:10px;">
                <div style="padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);">
                  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
                    <span style="font-size:16px;">🇨🇳</span>
                    <span style="font-size:12px;font-weight:700;">阿里云 TTS</span>
                    <span class="tag tag-green" style="font-size:9px;">推荐中文</span>
                  </div>
                  <div style="font-size:10px;color:var(--text3);">中文最自然，支持情感控制</div>
                </div>
                <div style="padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);">
                  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
                    <span style="font-size:16px;">🌍</span>
                    <span style="font-size:12px;font-weight:700;">ElevenLabs</span>
                    <span class="tag tag-blue" style="font-size:9px;">多语言</span>
                  </div>
                  <div style="font-size:10px;color:var(--text3);">情感丰富，支持声音克隆</div>
                </div>
                <div style="padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);">
                  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
                    <span style="font-size:16px;">🆓</span>
                    <span style="font-size:12px;font-weight:700;">Edge TTS</span>
                    <span class="tag tag-purple" style="font-size:9px;">免费</span>
                  </div>
                  <div style="font-size:10px;color:var(--text3);">微软免费方案，速度快</div>
                </div>
                <div style="padding:12px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);">
                  <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
                    <span style="font-size:16px;">🤖</span>
                    <span style="font-size:12px;font-weight:700;">Azure TTS</span>
                    <span class="tag tag-orange" style="font-size:9px;">企业级</span>
                  </div>
                  <div style="font-size:10px;color:var(--text3);">高稳定性，SSML 细粒度控制</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Right Preview Panel -->
          <div class="voice-preview-panel">
            <div style="padding:14px 16px;border-bottom:1px solid var(--border);">
              <div style="font-size:13px;font-weight:700;">🔊 音频预览</div>
              <div style="font-size:11px;color:var(--text3);margin-top:2px;">镜头 01 · 女声-温暖</div>
            </div>
            <div class="waveform-area">
              <script>/* waveform bars */</script>
            </div>
            <div class="voice-controls">
              <button class="play-btn">▶</button>
              <span class="time-display">00:00 / 00:04</span>
              <div style="flex:1;"></div>
              <button class="btn btn-sm btn-ghost">📥 导出音频</button>
            </div>
            <div class="voice-settings">
              <div class="setting-row">
                <span class="sr-label">TTS 平台</span>
                <span class="sr-value">ElevenLabs</span>
              </div>
              <div class="setting-row">
                <span class="sr-label">声音模型</span>
                <span class="sr-value">Rachel — 温暖女声</span>
              </div>
              <div class="setting-row">
                <span class="sr-label">语速</span>
                <span class="sr-value">1.0x（正常）</span>
              </div>
              <div class="setting-row">
                <span class="sr-label">情感</span>
                <span class="sr-value">温暖、有说服力</span>
              </div>
              <div class="setting-row">
                <span class="sr-label">音量</span>
                <span class="sr-value">80%</span>
              </div>
              <div class="setting-row">
                <span class="sr-label">输出格式</span>
                <span class="sr-value">MP3 · 320kbps</span>
              </div>
            </div>
            <div style="padding:16px;">
              <button class="btn btn-primary" style="width:100%;justify-content:center;">🎵 批量生成全部配音</button>
            </div>
          </div>
        </div>
      </div>

      <!-- ========== PAGE: EXPORT ========== -->
      <div class="page" id="page-export">
        <div class="page-header">
          <h1>导出中心</h1>
          <p>多规格一键导出、A/B 变体批量生成、投放平台适配</p>
        </div>

        <!-- Aspect Ratio Selection -->
        <div class="card" style="margin-bottom:20px;">
          <div class="card-header"><h3>📐 选择导出规格</h3></div>
          <div class="export-grid">
            <div class="export-card selected" onclick="this.parentElement.querySelectorAll('.export-card').forEach(c=>c.classList.remove('selected'));this.classList.add('selected');">
              <div class="ec-ratio ratio-916"></div>
              <div class="ec-label">9:16 竖版</div>
              <div class="ec-desc">抖音 / TikTok / Instagram Reels</div>
              <div class="ec-size">1080 × 1920</div>
            </div>
            <div class="export-card" onclick="this.parentElement.querySelectorAll('.export-card').forEach(c=>c.classList.remove('selected'));this.classList.add('selected');">
              <div class="ec-ratio ratio-169"></div>
              <div class="ec-label">16:9 横版</div>
              <div class="ec-desc">YouTube / B站 / 网页广告</div>
              <div class="ec-size">1920 × 1080</div>
            </div>
            <div class="export-card" onclick="this.parentElement.querySelectorAll('.export-card').forEach(c=>c.classList.remove('selected'));this.classList.add('selected');">
              <div class="ec-ratio ratio-11"></div>
              <div class="ec-label">1:1 方形</div>
              <div class="ec-desc">Instagram Feed / 微信朋友圈</div>
              <div class="ec-size">1080 × 1080</div>
            </div>
          </div>
        </div>

        <!-- A/B Variants -->
        <div class="card" style="margin-bottom:20px;">
          <div class="card-header">
            <h3>🧪 A/B 变体</h3>
            <button class="btn btn-sm btn-secondary">+ 添加变体</button>
          </div>
          <div style="display:flex;flex-direction:column;gap:10px;">
            <div class="ab-variant-row">
              <div class="ab-label" style="background:linear-gradient(135deg,#6c63ff,#4facfe);color:#fff;">A</div>
              <div class="ab-info">
                <h4>原始版本</h4>
                <p>标准 AIDA 结构，痛点引入 → 产品展示 → 信任背书 → CTA</p>
              </div>
              <span class="tag tag-green">30s · 已就绪</span>
            </div>
            <div class="ab-variant-row">
              <div class="ab-label" style="background:linear-gradient(135deg,#f7971e,#ff6b6b);color:#fff;">B</div>
              <div class="ab-info">
                <h4>功能展示变体</h4>
                <p>直接展示 App 界面操作流程，跳过痛点环节，快速进入产品演示</p>
              </div>
              <span class="tag tag-orange">25s · 待配音</span>
            </div>
          </div>
        </div>

        <!-- Platform Adaptation -->
        <div class="card" style="margin-bottom:20px;">
          <div class="card-header"><h3>📱 投放平台适配</h3></div>
          <div class="grid-3" style="gap:10px;">
            <div style="padding:14px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);">
              <div style="font-size:14px;font-weight:700;margin-bottom:6px;">TikTok</div>
              <div style="font-size:11px;color:var(--text2);line-height:1.6;">
                ✅ 竖版 9:16<br>
                ✅ 前 3 秒高能钩子<br>
                ✅ 无敏感金融词汇<br>
                ⚠️ 需添加风险提示
              </div>
            </div>
            <div style="padding:14px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);">
              <div style="font-size:14px;font-weight:700;margin-bottom:6px;">Instagram</div>
              <div style="font-size:11px;color:var(--text2);line-height:1.6;">
                ✅ 方形 + 竖版<br>
                ✅ 15s Reels 版本<br>
                ✅ 品牌调性一致<br>
                ⚠️ 15s 需精简文案
              </div>
            </div>
            <div style="padding:14px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);">
              <div style="font-size:14px;font-weight:700;margin-bottom:6px;">YouTube</div>
              <div style="font-size:11px;color:var(--text2);line-height:1.6;">
                ✅ 横版 16:9<br>
                ✅ 可扩展至 60s<br>
                ✅ 含前贴片/中插<br>
                ⚠️ 需跳过按钮友好
              </div>
            </div>
          </div>
        </div>

        <!-- Export Summary -->
        <div class="export-summary">
          <h3>📤 导出清单</h3>
          <div class="export-items">
            <div class="export-item">
              <span class="ei-icon">📹</span>
              <div class="ei-info">
                <div class="ei-name">PayEase_Wallet_A_9x16.mp4</div>
                <div class="ei-detail">1080×1920 · 30s · H.264 · 版本 A</div>
              </div>
              <span class="ei-status tag tag-green">就绪</span>
            </div>
            <div class="export-item">
              <span class="ei-icon">📹</span>
              <div class="ei-info">
                <div class="ei-name">PayEase_Wallet_A_16x9.mp4</div>
                <div class="ei-detail">1920×1080 · 30s · H.264 · 版本 A</div>
              </div>
              <span class="ei-status tag tag-green">就绪</span>
            </div>
            <div class="export-item">
              <span class="ei-icon">📹</span>
              <div class="ei-info">
                <div class="ei-name">PayEase_Wallet_A_1x1.mp4</div>
                <div class="ei-detail">1080×1080 · 30s · H.264 · 版本 A</div>
              </div>
              <span class="ei-status tag tag-green">就绪</span>
            </div>
            <div class="export-item">
              <span class="ei-icon">🎬</span>
              <div class="ei-info">
                <div class="ei-name">PayEase_Wallet_B_9x16.mp4</div>
                <div class="ei-detail">1080×1920 · 25s · H.264 · 版本 B</div>
              </div>
              <span class="ei-status tag tag-orange">待配音</span>
            </div>
            <div class="export-item">
              <span class="ei-icon">🖼️</span>
              <div class="ei-info">
                <div class="ei-name">PayEase_Wallet_Cover.png</div>
                <div class="ei-detail">1080×1920 · 封面图</div>
              </div>
              <span class="ei-status tag tag-green">就绪</span>
            </div>
            <div class="export-item">
              <span class="ei-icon">📋</span>
              <div class="ei-info">
                <div class="ei-name">PayEase_Wallet_Storyboard.csv</div>
                <div class="ei-detail">分镜脚本导出</div>
              </div>
              <span class="ei-status tag tag-green">就绪</span>
            </div>
          </div>
          <div style="display:flex;gap:10px;margin-top:20px;">
            <button class="btn btn-primary" style="flex:1;justify-content:center;" onclick="showToast('开始导出...')">📤 一键导出全部就绪文件</button>
            <button class="btn btn-secondary" onclick="showToast('已添加到导出队列')">仅导出就绪项</button>
          </div>
        </div>
      </div>

    </div><!-- /content-area -->
  </div><!-- /main-area -->
</div><!-- /app-layout -->

<!-- ========== NEW PROJECT MODAL ========== -->
<div class="modal-overlay" id="modal-new-project">
  <div class="modal">
    <div class="modal-header">
      <h3>新建广告项目</h3>
      <button class="modal-close" onclick="closeModal('modal-new-project')">✕</button>
    </div>
    <div class="modal-body">
      <div class="input-group">
        <label>产品名称</label>
        <input class="input-field" placeholder="例如：PayEase Wallet">
      </div>
      <div class="input-group">
        <label>产品类型</label>
        <select class="input-field">
          <option>💳 数字钱包</option>
          <option>📈 理财平台</option>
          <option>🪙 加密资产/交易平台</option>
          <option>🏦 跨境支付</option>
          <option>🛡️ 保险科技</option>
          <option>📦 其他金融产品</option>
        </select>
      </div>
      <div class="input-group">
        <label>目标市场</label>
        <select class="input-field">
          <option>🇸🇬 东南亚（新加坡/印尼/泰国/越南）</option>
          <option>🇺🇸 北美（美国/加拿大）</option>
          <option>🇦🇪 中东（阿联酋/沙特）</option>
          <option>🇯🇵 日本</option>
          <option>🇰🇷 韩国</option>
          <option>🌍 全球多市场</option>
        </select>
      </div>
      <div class="input-group">
        <label>视频时长</label>
        <div style="display:flex;gap:8px;">
          <button class="btn btn-secondary" style="flex:1;">15s</button>
          <button class="btn btn-primary" style="flex:1;">30s</button>
          <button class="btn btn-secondary" style="flex:1;">60s</button>
          <button class="btn btn-secondary" style="flex:1;">90s</button>
        </div>
      </div>
      <div class="input-group">
        <label>广告模板</label>
        <div style="display:flex;gap:8px;">
          <button class="btn btn-secondary" style="flex:1;">AIDA</button>
          <button class="btn btn-secondary" style="flex:1;">PAS</button>
          <button class="btn btn-secondary" style="flex:1;">自定义</button>
        </div>
      </div>
      <div class="upload-zone" style="margin-top:8px;">
        <div class="upload-icon">📱</div>
        <div class="upload-text">上传产品截图和品牌素材</div>
        <div class="upload-hint">App 界面截图、Logo、品牌指南（可选，后续也可上传）</div>
      </div>
    </div>
    <div class="modal-footer">
      <button class="btn btn-secondary" onclick="closeModal('modal-new-project')">取消</button>
      <button class="btn btn-primary" onclick="closeModal('modal-new-project');showToast('项目创建成功')">创建项目</button>
    </div>
  </div>
</div>

<!-- ========== TOAST ========== -->
<div id="toast" style="position:fixed;bottom:32px;left:50%;transform:translateX(-50%) translateY(80px);background:rgba(108,99,255,.95);color:#fff;padding:12px 24px;border-radius:10px;font-size:13px;font-weight:600;z-index:9999;transition:transform .4s ease,opacity .4s ease;opacity:0;pointer-events:none;box-shadow:0 8px 24px rgba(108,99,255,.4);"></div>

<script>
// Page Switching
function switchPage(pageId, navEl) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.getElementById('page-' + pageId).classList.add('active');
  document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
  if (navEl) navEl.classList.add('active');

  // Update breadcrumb
  const names = {
    dashboard: '项目列表',
    script: '剧本编辑 — PayEase Wallet',
    style: '全局风格设定',
    scenes: '场景资产管理',
    storyboard: '分镜脚本',
    voiceover: '配音工作台',
    export: '导出中心'
  };
  document.getElementById('breadcrumb-current').textContent = names[pageId] || pageId;
}

// Modal
function openNewProjectModal() {
  document.getElementById('modal-new-project').classList.add('show');
}
function closeModal(id) {
  document.getElementById(id).classList.remove('show');
}
document.getElementById('modal-new-project').addEventListener('click', function(e) {
  if (e.target === this) closeModal('modal-new-project');
});

// Toast
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.style.transform = 'translateX(-50%) translateY(0)';
  t.style.opacity = '1';
  setTimeout(() => {
    t.style.transform = 'translateX(-50%) translateY(80px)';
    t.style.opacity = '0';
  }, 2500);
}

// Clip selection
function selectClip(el, num) {
  document.querySelectorAll('.clip').forEach(c => c.classList.remove('selected'));
  el.classList.add('selected');
  document.querySelector('.clip-detail-header h3').textContent = '镜头 0' + num + ' 详情';
  // Update preview icon based on clip
  const icons = ['🎬', '📱', '🌍', '✅'];
  document.getElementById('clip-preview').textContent = icons[num-1] || '🎬';
}

// Simulate upload
function simulateUpload() {
  const container = document.getElementById('uploaded-files');
  const names = ['screenshot_home.png', 'wallet_balance.jpg', 'transfer_flow.png', 'app_icon.png'];
  const sizes = ['1.6 MB', '2.1 MB', '1.3 MB', '0.5 MB'];
  const icons = ['📱', '📱', '📱', '🖼️'];
  const i = Math.floor(Math.random() * names.length);
  const file = document.createElement('div');
  file.className = 'uploaded-file';
  file.style.animation = 'pageFadeIn .3s ease';
  file.innerHTML = '<span class="file-icon">' + icons[i] + '</span><span class="file-name">' + names[i] + '</span><span class="file-size">' + sizes[i] + '</span><span class="file-remove" onclick="this.parentElement.remove()">✕</span>';
  container.appendChild(file);
  showToast('素材上传成功');
}

// Generate waveform bars
(function() {
  const waveform = document.querySelector('.waveform-area');
  if (!waveform) return;
  for (let i = 0; i < 60; i++) {
    const bar = document.createElement('div');
    bar.className = 'waveform-bar';
    bar.style.height = (15 + Math.random() * 60) + 'px';
    bar.style.animationDelay = (Math.random() * 1.5) + 's';
    waveform.appendChild(bar);
  }
})();

// Keyboard shortcut
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    document.querySelectorAll('.modal-overlay.show').forEach(m => m.classList.remove('show'));
  }
  if (e.ctrlKey && e.key === 's') {
    e.preventDefault();
    showToast('项目已保存');
  }
});
</script>
</body>
</html>'''

output_path = '/Users/xiaowu/WorkBuddy/Claw/ad-video-product/app/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Verify
import re
with open(output_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"File size: {len(content)} chars")
print(f"Lines: {content.count(chr(10)) + 1}")
print(f"Ends with </html>: {content.strip().endswith('</html>')}")
print(f"All pages present: {all(f'id=\"page-{p}\"' in content for p in ['dashboard','script','style','scenes','storyboard','voiceover','export'])}")
print(f"HTML tags balanced: {content.count('<html') == content.count('</html>')}")
print(f"Body tags balanced: {content.count('<body') == content.count('</body>')}")
print(f"Script tags balanced: {content.count('<script') == content.count('</script>')}")
print(f"Style tags balanced: {content.count('<style') == content.count('</style>')}")
print(f"Modal present: {'modal-new-project' in content}")
print(f"Toast present: {'toast' in content}")
print(f"Upload zone: {'upload-zone' in content}")
print(f"Phone mockup: {'phone-mockup' in content}")
print(f"Compliance bar: {'compliance-bar' in content}")
print(f"A/B variant: {'ab-variant' in content}")
print(f"Scene cards: {'scene-card' in content}")
print(f"Storyboard timeline: {'timeline-track' in content}")
print(f"Voiceover lines: {'voice-line' in content}")
print(f"Export summary: {'export-summary' in content}")
print("Done!")
