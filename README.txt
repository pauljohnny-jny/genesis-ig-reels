Genesis IG – recovery package for pauljohnny-jny/genesis-ig-reels (base: main fddb336198be6d07f0d2aba4f484cee9477e03db)
Local head: cd1667f52b822e7c5ccc99e2dbadbef94d05cdba (5 commits on top of fddb336).

Choose ONE way to apply:
A) git:  git fetch <path>/genesis-batch-19-38.bundle main:recovery && git merge --ff-only recovery && git push origin main
B) git am --3way patches/*.patch   (binary patches; includes the 20 MP4s)
C) Browser: upload every file under files/ to the same path in the repo (reels/, captions/, toolkit/specs/, PLAN.md). Do not rename or re-encode.

Verify after pushing (all must pass):
  cd reels && grep mp4 SHA256SUMS_batch_19-38_approved.txt | sha256sum -c
  cd .. && grep txt reels/SHA256SUMS_batch_19-38_approved.txt | sed 's#  #  captions/#' | sha256sum -c
Reel 22 caption must hash 2ec3f28893c65aabe7121b3995e7adddb232648fdf7cac1dbb7631137d03e675.
PLAN.md keeps fddb336's Reel 17/18 live rows unchanged.
