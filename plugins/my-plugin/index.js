/**
 * my-plugin — Custom Claude Code plugin
 *
 * Hooks into PreToolUse and PostToolUse lifecycle events to add
 * project-specific behaviour (logging, validation, notifications).
 */

module.exports = {
  name: 'my-plugin',
  version: '0.1.0',

  /**
   * Called before any tool is executed.
   * Return { block: true, reason: '...' } to prevent execution.
   */
  async preToolUse({ tool, input }) {
    // Example: block writes to sensitive paths
    if (tool === 'Write' && input.file_path?.includes('.env')) {
      console.warn('[my-plugin] Blocked direct write to .env file');
      return { block: true, reason: 'Direct writes to .env files are not allowed.' };
    }
    return { block: false };
  },

  /**
   * Called after any tool completes successfully.
   */
  async postToolUse({ tool, input, output }) {
    if (tool === 'Write') {
      console.info(`[my-plugin] File written: ${input.file_path}`);
    }
  },
};
