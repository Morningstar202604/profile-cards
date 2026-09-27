<svg xmlns="http://www.w3.org/2000/svg" width="640" height="$HEIGHT" viewBox="0 0 640 $HEIGHT" role="img" aria-label="Open Source Impact Card — $USER">
  $BG
  <defs>$NUMG</defs>

  <path d="M26 40 l4 -5 l4 5 l-4 5 z" fill="$GOLD_BRIGHT" opacity="0.95"/>
  <text x="40" y="44" font-family="'Segoe UI',Helvetica,Arial,'PingFang SC','Microsoft YaHei',sans-serif" font-size="14.5" font-weight="700" letter-spacing="3" fill="$GOLD_BRIGHT">OPEN SOURCE IMPACT</text>
  <text x="610" y="44" text-anchor="end" font-family="'Segoe UI',Helvetica,Arial,'PingFang SC','Microsoft YaHei',sans-serif" font-size="10.5" letter-spacing="1" fill="$SUB">更新于 $DATE</text>
  <text x="40" y="70" font-family="'Segoe UI',Helvetica,Arial,'PingFang SC','Microsoft YaHei',sans-serif" font-size="17" font-weight="600" fill="$TEXT">$USER</text>
  <text x="610" y="70" text-anchor="end" font-family="'Segoe UI',Helvetica,Arial,'PingFang SC','Microsoft YaHei',sans-serif" font-size="11" letter-spacing="1" fill="$SUB">GitHub · 已合并 PR</text>

  <line x1="40" y1="84" x2="600" y2="84" stroke="$LINE" stroke-width="1"/>
  <line x1="286" y1="83" x2="354" y2="83" stroke="$GOLD" stroke-width="1.4" opacity="0.8"/>
  <path d="M320 80 l4 4 l-4 4 l-4 -4 z" fill="$GOLD" opacity="0.9"/>

  <rect x="30" y="98" width="180" height="82" rx="10" fill="url(#ppanel)" stroke="$LINE"/>
  <line x1="88" y1="98" x2="152" y2="98" stroke="$GOLD" stroke-width="2" opacity="0.7"/>
  <text x="194" y="114" text-anchor="end" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="9.5" letter-spacing="1.5" fill="$DIM">01</text>
  <text x="120" y="148" text-anchor="middle" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="28" font-weight="600" fill="url(#gtimp)">$PR_COUNT</text>
  <text x="120" y="168" text-anchor="middle" font-family="'PingFang SC','Microsoft YaHei','Segoe UI',sans-serif" font-size="11" letter-spacing="2" fill="$MUTED">合并 PR</text>

  <rect x="230" y="98" width="180" height="82" rx="10" fill="url(#ppanel)" stroke="$LINE"/>
  <line x1="288" y1="98" x2="352" y2="98" stroke="$GOLD" stroke-width="2" opacity="0.7"/>
  <text x="394" y="114" text-anchor="end" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="9.5" letter-spacing="1.5" fill="$DIM">02</text>
  <text x="320" y="148" text-anchor="middle" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="28" font-weight="600" fill="url(#gtimp)">$REPO_COUNT</text>
  <text x="320" y="168" text-anchor="middle" font-family="'PingFang SC','Microsoft YaHei','Segoe UI',sans-serif" font-size="11" letter-spacing="2" fill="$MUTED">贡献仓库</text>

  <rect x="430" y="98" width="180" height="82" rx="10" fill="url(#ppanel)" stroke="$LINE"/>
  <line x1="488" y1="98" x2="552" y2="98" stroke="$GOLD" stroke-width="2" opacity="0.7"/>
  <text x="594" y="114" text-anchor="end" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="9.5" letter-spacing="1.5" fill="$DIM">03</text>
  <text x="520" y="148" text-anchor="middle" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="24" font-weight="600" fill="url(#gtimp)">$IMPACT</text>
  <text x="520" y="168" text-anchor="middle" font-family="'PingFang SC','Microsoft YaHei','Segoe UI',sans-serif" font-size="11" letter-spacing="2" fill="$MUTED">影响力 · Σ 仓库 star</text>

  <path d="M30 200 l3.5 -4 l3.5 4 l-3.5 4 z" fill="$GOLD" opacity="0.9"/>
  <text x="42" y="204" font-family="'PingFang SC','Microsoft YaHei','Segoe UI',sans-serif" font-size="13" font-weight="600" letter-spacing="2" fill="$GOLD">贡献分档 · 按仓库 star</text>
  $TIER_BOXES

  <path d="M30 296 l3.5 -4 l3.5 4 l-3.5 4 z" fill="$GOLD" opacity="0.9"/>
  <text x="42" y="300" font-family="'PingFang SC','Microsoft YaHei','Segoe UI',sans-serif" font-size="13" font-weight="600" letter-spacing="2" fill="$GOLD">TOP 贡献仓库</text>
  $TOP_ROWS
  $RECENT_LINE

  <line x1="40" y1="$FOOTER_Y" x2="600" y2="$FOOTER_Y" stroke="$LINE" stroke-width="0.8"/>
  <text x="40" y="$FOOTER_Y2" font-family="'PingFang SC','Microsoft YaHei','Segoe UI',sans-serif" font-size="10" fill="$DIM">数据来源 GitHub API · 每日自动刷新 · 零服务器自动生成</text>
  <text x="600" y="$FOOTER_Y2" text-anchor="end" font-family="'Segoe UI',Helvetica,Arial,sans-serif" font-size="10" letter-spacing="1.5" fill="$DIM">impact-card · v1.4.1</text>
</svg>
