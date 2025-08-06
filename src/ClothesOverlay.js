import React from "react";

function ClothesOverlay({ height, clothes }) {
  // 아바타 키(실제)와 SVG 키(200px) 비율
  const avatarHeightPx = 200;
  const avatarTopY = 30 + 24 * 2; // 머리 아래
  const centerX = 110;

  // 실측값(cm) → px 변환 (키 기준)
  const pxPerCm = avatarHeightPx / height;
  const clothesWidth = clothes.chest * 2 * pxPerCm; // 가슴단면*2 = 가슴둘레
  const clothesShoulder = clothes.shoulder * pxPerCm;
  const clothesLength = clothes.length * pxPerCm;

  return (
    <g>
      {/* 어깨선 */}
      <rect x={centerX - clothesShoulder / 2} y={avatarTopY} width={clothesShoulder} height={6} fill="#ffb6b6" fillOpacity={0.7} />
      {/* 몸통(가슴둘레) */}
      <rect x={centerX - clothesWidth / 2} y={avatarTopY + 6} width={clothesWidth} height={clothesLength - 6} fill="#ffb6b6" fillOpacity={0.35} stroke="#e57373" strokeDasharray="4 2" />
    </g>
  );
}

export default ClothesOverlay; 