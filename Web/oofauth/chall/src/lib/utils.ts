export const createLoadObserver = (handler) => {
  let waiting = 0;

  const onload = (el) => {
    waiting++;
    el.addEventListener("load", () => {
      waiting--;
      if (waiting === 0) {
        handler();
      }
    });
  };

  return onload;
};

// array just to increase security by obscurity
export const reverse = (s: string[]) => {
  let x = s.join(''); 
  const length = x.length;
  for(let i = 0; i < Math.floor(length / 2); i++) {
    const temp = x[i]
    x = x.substring(0, i) + 
      x.charAt(length - i - 1) +  
      x.substring(i + 1, length - i - 1) + 
      temp + 
      x.substring(length - i)
  }
  return x
};

const b64_table =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";

const b64_encode = (data) => {
  let o1, o2, o3, h1, h2, h3, h4, bits, r, i = 0, enc = "";
  if (!data) {
    return data;
  }
  do {
    o1 = data[i++];
    o2 = data[i++];
    o3 = data[i++];
    bits = o1 << 16 | o2 << 8 | o3;
    h1 = bits >> 18 & 0x3f;
    h2 = bits >> 12 & 0x3f;
    h3 = bits >> 6 & 0x3f;
    h4 = bits & 0x3f;
    enc += b64_table.charAt(h1) + b64_table.charAt(h2) + b64_table.charAt(h3) +
      b64_table.charAt(h4);
  } while (i < data.length);
  r = data.length % 3;
  return (r ? enc.slice(0, r - 3) : enc) + "===".slice(r || 3);
};

const b64_decode = (data) => {
  let o1, o2, o3, h1, h2, h3, h4, bits, i = 0, result = [];
  if (!data) {
    return data;
  }
  data += "";
  do {
    h1 = b64_table.indexOf(data.charAt(i++));
    h2 = b64_table.indexOf(data.charAt(i++));
    h3 = b64_table.indexOf(data.charAt(i++));
    h4 = b64_table.indexOf(data.charAt(i++));
    bits = h1 << 18 | h2 << 12 | h3 << 6 | h4;
    o1 = bits >> 16 & 0xff;
    o2 = bits >> 8 & 0xff;
    o3 = bits & 0xff;
    result.push(o1);
    if (h3 !== 64) {
      result.push(o2);
      if (h4 !== 64) {
        result.push(o3);
      }
    }
  } while (i < data.length);
  return result;
};

export const xorEncode = (key: string, data: string): string => {
  data = xor_encrypt(key, data);
  return b64_encode(data);
};

export const xorDecode = (key: string, data: string): string => {
  data = b64_decode(data);
  return xor_decrypt(key, data);
};

const keyCharAt = (key, i) => {
  return key.charCodeAt(Math.floor(i % key.length));
};

const xor_encrypt = (key, data) => {
  return Array.prototype.map.call(data, (c, i) => {
    return c.charCodeAt(0) ^ keyCharAt(key, i);
  });
};

const xor_decrypt = (key, data) => {
  return Array.prototype.map.call(data, (c, i) => {
    return String.fromCharCode(c ^ keyCharAt(key, i));
  }).join("");
};
