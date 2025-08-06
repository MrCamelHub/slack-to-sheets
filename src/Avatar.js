import React from "react";

function Avatar({ height, weight }) {
  // 아바타의 전체 키를 200px로 정규화
  const avatarHeightPx = 200;
  // 몸통, 머리, 팔다리 비율을 단순화
  const headRadius = 24;
  const bodyWidth = 40 + (weight - 20) * 0.8; // 몸무게에 따라 몸통 너비 변화
  const bodyHeight = avatarHeightPx * 0.45;
  const legHeight = avatarHeightPx * 0.35;
  const armLength = avatarHeightPx * 0.38;
  const centerX = 110;
  const topY = 30;

  return (
    <g>
      {/* 머리 */}
      <circle cx={centerX} cy={topY + headRadius} r={headRadius} fill="#ffe0b2" stroke="#d2a679" strokeWidth={2} />
      {/* 몸통 */}
      <rect x={centerX - bodyWidth / 2} y={topY + headRadius * 2} width={bodyWidth} height={bodyHeight} rx={bodyWidth * 0.2} fill="#90caf9" stroke="#1976d2" strokeWidth={2} />
      {/* 팔 */}
      <rect x={centerX - bodyWidth / 2 - 18} y={topY + headRadius * 2 + 18} width={16} height={armLength} rx={8} fill="#ffe0b2" stroke="#d2a679" strokeWidth={2} />
      <rect x={centerX + bodyWidth / 2 + 2} y={topY + headRadius * 2 + 18} width={16} height={armLength} rx={8} fill="#ffe0b2" stroke="#d2a679" strokeWidth={2} />
      {/* 다리 */}
      <rect x={centerX - bodyWidth / 2 + 6} y={topY + headRadius * 2 + bodyHeight} width={12} height={legHeight} rx={6} fill="#ffe0b2" stroke="#d2a679" strokeWidth={2} />
      <rect x={centerX + bodyWidth / 2 - 18} y={topY + headRadius * 2 + bodyHeight} width={12} height={legHeight} rx={6} fill="#ffe0b2" stroke="#d2a679" strokeWidth={2} />
    </g>
  );
}

export default Avatar; 