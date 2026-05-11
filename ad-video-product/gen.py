#!/usr/bin/env python3
import os

out = "/Users/xiaowu/WorkBuddy/Claw/ad-video-product/app/index.html"
os.makedirs(os.path.dirname(out), exist_ok=True)

parts = []

# ===== HEAD + CSS =====
parts.append("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>AdCraft Studio — 境外金融产品广告视频制作平台</title>
<style>
:root {
  --bg:#0a0b10;--bg2:#11131b;--bg3:#181b27;--bg4:#1e2235;
  --border:#252a3a;--border-light:#313752;
  --accent:#6c63ff;--accent-hover:#7b73ff;
  --accent2:#ff6b6b;--accent3:#43e97b;--accent4:#f7971e;
  --accent5:#4facfe;--accent6:#e040fb;--gold:#f0c040;
  --text:#e8eaf0;--text2:#9499ad;--text3:#5a6078;
  --radius:12px;--radius-sm:8px;
  --transition:all .25s cubic-bezier(.4,0,.2,1);
}
* {box-sizing:border-box;margin:0;padding:0;}
body {background:var(--bg);color:var(--text);font-family:-apple-system,BlinkMacSystemFont,'PingFang SC',sans-serif;line-height:1.6;overflow:hidden;height:100vh;}
button {cursor:pointer;font-family:inherit;}
.app-layout {display:flex;height:100vh;overflow:hidden;}

/* SIDEBAR */
.sidebar {width:240px;background:var(--bg2);border-right:1px solid var(--border);display:flex;flex-direction:column;flex-shrink:0;}
.sidebar-header {padding:16px 20px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px;}
.sidebar-logo {width:32px;height:32px;background:linear-gradient(135deg,#6c63ff,#4facfe);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:16px;font-weight:900;color:#fff;}
.sidebar-brand {font-size:15px;font-weight:800;color:#fff;}
.sidebar-brand small {display:block;font-size:10px;color:var(--text3);font-weight:500;}
.sidebar-nav {flex:1;padding:12px 10px;overflow-y:auto;}
.nav-section {margin-bottom:16px;}
.nav-section-label {font-size:10px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:1.5px;padding:4px 10px 8px;}
.nav-item {display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:var(--radius-sm);color:var(--text2);font-size:13px;font-weight:500;transition:var(--transition);cursor:pointer;border:1px solid transparent;position:relative;}
.nav-item:hover {background:rgba(108,99,255,.06);color:var(--text);}
.nav-item.active {background:rgba(108,99,255,.1);color:#fff;border-color:rgba(108,99,255,.25);}
.nav-item.active::before {content:'';position:absolute;left:-10px;top:50%;transform:translateY(-50%);width:3px;height:20px;background:var(--accent);border-radius:0 3px 3px 0;}
.nav-item .nav-icon {width:28px;height:28px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:14px;background:var(--bg3);flex-shrink:0;}
.nav-item.active .nav-icon {background:rgba(108,99,255,.25);}
.nav-badge {margin-left:auto;font-size:10px;font-weight:700;padding:2px 7px;border-radius:10px;background:rgba(67,233,123,.15);color:#43e97b;}
.nav-badge.warn {background:rgba(247,151,30,.15);color:#f7971e;}
.sidebar-footer {padding:12px;border-top:1px solid var(--border);}
.sidebar-user {display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:var(--radius-sm);transition:var(--transition);cursor:pointer;}
.sidebar-user:hover {background:var(--bg3);}
.user-avatar {width:32px;height:32px;border-radius:50%;background:linear-gradient(135deg,#f7971e,#ff6b6b);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#fff;}
.user-info .name {font-size:12px;font-weight:600;color:var(--text);}
.user-info .role {font-size:10px;color:var(--text3);}

/* MAIN */
.main-area {flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0;}
.topbar {height:56px;background:rgba(10,11,16,.85);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);display:flex;align-items:center;padding:0 24px;gap:16px;flex-shrink:0;z-index:50;}
.topbar-breadcrumb {display:flex;align-items:center;gap:8px;flex:1;}
.breadcrumb-item {font-size:13px;color:var(--text3);}
.breadcrumb-item.current {color:var(--text);font-weight:600;}
.breadcrumb-sep {color:var(--text3);font-size:11px;}
.topbar-actions {display:flex;align-items:center;gap:8px;}
.topbar-btn {width:36px;height:36px;border-radius:var(--radius-sm);border:1px solid var(--border);background:var(--bg2);display:flex;align-items:center;justify-content:center;color:var(--text2);font-size:16px;transition:var(--transition);}
.topbar-btn:hover {border-color:var(--accent);color:var(--accent);}
.topbar-btn.primary {background:linear-gradient(135deg,#6c63ff,#4facfe);border:none;color:#fff;}
.content-area {flex:1;overflow-y:auto;padding:24px;}
.page {display:none;animation:pageIn .35s ease;}
.page.active {display:block;}
@keyframes pageIn {from{opacity:0;transform:translateY(12px);} to{opacity:1;transform:translateY(0);}}

/* COMMON */
.page-header {margin-bottom:24px;}
.page-header h1 {font-size:22px;font-weight:800;margin-bottom:4px;}
.page-header p {font-size:13px;color:var(--text2);}
.card {background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:20px;transition:var(--transition);}
.card-header {display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;}
.card-header h3 {font-size:15px;font-weight:700;}
.card-action {font-size:12px;color:var(--accent);cursor:pointer;display:flex;align-items:center;gap:4px;}
.card-action:hover {color:var(--accent-hover);}
.grid-2 {display:grid;grid-template-columns:1fr 1fr;gap:16px;}
.grid-3 {display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;}
.btn {display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:var(--radius-sm);font-size:13px;font-weight:600;transition:var(--transition);border:none;cursor:pointer;}
.btn-primary {background:linear-gradient(135deg,#6c63ff,#4facfe);color:#fff;}
.btn-primary:hover {box-shadow:0 4px 16px rgba(108,99,255,.35);transform:translateY(-1px);}
.btn-secondary {background:var(--bg3);border:1px solid var(--border);color:var(--text);}
.btn-secondary:hover {border-color:var(--accent);}
.btn-sm {padding:5px 12px;font-size:12px;}
.tag {display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:6px;font-size:11px;font-weight:600;}
.tag-purple {background:rgba(108,99,255,.12);color:#a09bff;}
.tag-green {background:rgba(67,233,123,.1);color:#43e97b;}
.tag-orange {background:rgba(247,151,30,.1);color:#f7971e;}
.tag-blue {background:rgba(79,172,254,.1);color:#4facfe;}
.tag-red {background:rgba(255,107,107,.1);color:#ff6b6b;}
.tag-gold {background:rgba(240,192,64,.12);color:var(--gold);}
.stat-card {background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:20px;transition:var(--transition);}
.stat-icon {width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;margin-bottom:12px;}
.stat-value {font-size:28px;font-weight:800;margin-bottom:2px;}
.stat-label {font-size:12px;color:var(--text3);}
.input-group {margin-bottom:14px;}
.input-group label {display:block;font-size:12px;font-weight:600;color:var(--text2);margin-bottom:6px;}
.input-field {width:100%;padding:9px 13px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);color:var(--text);font-size:13px;outline:none;transition:var(--transition);}
.input-field:focus {border-color:var(--accent);box-shadow:0 0 0 3px rgba(108,99,255,.15);}
.tabs {display:flex;gap:4px;margin-bottom:20px;background:var(--bg2);padding:4px;border-radius:var(--radius-sm);border:1px solid var(--border);}
.tab {padding:8px 16px;border-radius:6px;font-size:12px;font-weight:600;color:var(--text2);cursor:pointer;transition:var(--transition);border:none;background:transparent;}
.tab:hover {color:var(--text);}
.tab.active {background:rgba(108,99,255,.15);color:#fff;}
.progress-bar {height:6px;background:var(--bg3);border-radius:3px;overflow:hidden;}
.progress-bar .fill {height:100%;border-radius:3px;transition:width .6s ease;}
.upload-zone {border:2px dashed var(--border-light);border-radius:var(--radius);padding:24px;text-align:center;cursor:pointer;transition:var(--transition);}
.upload-zone:hover {border-color:var(--accent);background:rgba(108,99,255,.04);}
.upload-icon {font-size:28px;margin-bottom:8px;opacity:.6;}
.upload-text {font-size:13px;color:var(--text2);}
.upload-hint {font-size:11px;color:var(--text3);margin-top:4px;}
.uploaded-files {display:flex;flex-direction:column;gap:8px;margin-top:12px;}
.uploaded-file {display:flex;align-items:center;gap:10px;padding:8px 12px;background:var(--bg3);border:1px solid var(--border);border-radius:var(--radius-sm);font-size:12px;}
.file-icon {font-size:18px;}
.file-name {flex:1;color:var(--text);font-weight:500;}
.file-size {color:var(--text3);font-size:11px;}
.file-remove {color:var(--text3);cursor:pointer;font-size:14px;}
.file-remove:hover {color:#ff6b6b;}
.compliance-bar {background:rgba(240,192,64,.08);border:1px solid rgba(240,192,64,.2);border-radius:var(--radius);padding:12px 16px;display:flex;align-items:center;gap:10px;font-size:12px;color:var(--gold);margin-bottom:16px;}
.compliance-bar .cb-icon {font-size:16px;}
</style>
</head>
<body>
""")
