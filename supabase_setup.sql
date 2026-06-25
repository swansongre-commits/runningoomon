-- 러너 게임 랭킹 테이블 (Supabase)
-- 대시보드 → SQL Editor → New query 에 붙여넣고 Run 한 번만 실행하세요.

create table if not exists public.catgame_scores (
  id         bigint generated always as identity primary key,
  name       text    not null,
  score      integer not null,
  stage      integer not null default 1,
  created_at timestamptz not null default now()
);

-- RLS: 익명(anon, publishable 키) 사용자에게 읽기 + 등록만 허용
alter table public.catgame_scores enable row level security;

drop policy if exists "catgame anon read" on public.catgame_scores;
create policy "catgame anon read"
  on public.catgame_scores for select
  to anon
  using (true);

drop policy if exists "catgame anon insert" on public.catgame_scores;
create policy "catgame anon insert"
  on public.catgame_scores for insert
  to anon
  with check (char_length(name) between 1 and 16 and score >= 0 and score < 100000000);

-- TOP 10 정렬 가속용 인덱스
create index if not exists catgame_scores_score_idx on public.catgame_scores (score desc);
