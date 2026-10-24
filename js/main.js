// 근쌤의 서재 — 메인 페이지 동작 (JS가 없어도 내용은 모두 보이도록 만든다)

// 휴대폰 메뉴 열고 닫기
function initMenu() {
  const btn = document.getElementById('menuBtn');
  const panel = document.getElementById('menuPanel');
  if (!btn || !panel) return;

  const setOpen = (open) => {
    panel.hidden = !open;
    btn.setAttribute('aria-expanded', String(open));
    btn.textContent = open ? '닫기' : '메뉴';
  };

  btn.addEventListener('click', () => setOpen(panel.hidden));
  panel.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !panel.hidden) { setOpen(false); btn.focus(); } });
}

// 앱 목록: 5번째부터 접어 두고 "7개 모두 보기"로 펼침
function initAppList() {
  const list = document.getElementById('appList');
  const more = document.getElementById('appMore');
  if (!list || !more) return;

  list.classList.add('is-collapsed');
  more.hidden = false;
  more.addEventListener('click', () => {
    list.classList.remove('is-collapsed');
    more.hidden = true;
    list.querySelector('.extra a')?.focus();
  });
}

// 화면이 들어올 때 살짝 떠오름 (화면 밖에 있는 섹션만 잠시 기다리게 함)
function initReveal() {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !('IntersectionObserver' in window)) return;

  const sections = document.querySelectorAll('.reveal');
  const io = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.remove('is-pending');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  sections.forEach((section) => {
    const top = section.getBoundingClientRect().top;
    if (top > window.innerHeight) {
      section.classList.add('is-pending');
      io.observe(section);
    }
  });
}

// 쓴 글 탭 (AI · 교육 / 북리뷰) — 좌우 화살표로도 이동
function initTabs() {
  const tablist = document.querySelector('.tabs');
  if (!tablist) return;
  const tabs = [...tablist.querySelectorAll('[role="tab"]')];

  const select = (tab) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
  };

  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => select(tab));
    tab.addEventListener('keydown', (e) => {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      const next = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
      select(next);
      next.focus();
    });
  });

  tablist.hidden = false;
  tablist.parentElement.classList.add('tabs-ready');
  select(tabs[0]);
}

initMenu();
initAppList();
initTabs();
initReveal();
